class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    # add layer to network
    def add(self, layer):
        self.layers.append(layer)

    # set loss to use
    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    # prédit la sortie pour un ensemble d'entrées
    # input_data est un tableau de tableaux qui correspondent aux entrées
    # ex : [[0,0], [0,1], [1,0], [1,1]]
    # la sortie est un tableau de tableaux qui correspondent aux sorties
    # ex : [[0], [1], [1], [0]] pour le xor correspond à la sortie correcte
    def predict(self, input_data):

        # nombre d'échantillons dans le dataset
        samples = len(input_data)
        result = []

        # lance la propagation avant pour chaque échantillon
        # et stocke le résultat dans result
        for i in range(samples):
            result.append(self.predict_single(input_data[i]))

        return result
    
    # predict the output for a single input
    def predict_single(self, input_data):
        output = input_data
        for layer in self.layers:
            output = layer.forward_propagation(output)
        return output

    # entraine le réseau de neurones
    # x_train est un tableau de tableaux qui correspondent aux entrées
    # ex : [[0,0], [0,1], [1,0], [1,1]]
    # y_train est un tableau de tableaux qui correspondent aux sorties
    # ex : [[0], [1], [1], [0]] pour le xor correspond à la sortie correcte
    # epochs est le nombre d'itérations
    # learning_rate est le taux d'apprentissage

    # on récupère le nombre d'échantillons dans le dataset
    # on lance la propagation avant pour chaque échantillon
    # on calcule l'erreur
    # on lance la propagation arrière pour chaque échantillon
    # on calcule l'erreur moyenne sur tous les échantillons

    # résumé : [dataset] -> [propagation avant] -> [calcul erreur] -> [propagation arrière] -> [calcul erreur moyenne]

    def fit(self, x_train, y_train, epochs, learning_rate):
        # sample dimension first
        samples = len(x_train)

        # training loop
        for i in range(epochs):
            err = 0 # l'erreur totale

            # iterate over all samples
            for j in range(samples):
                # forward propagation
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                # compute loss (for display purpose only)
                err += self.loss(y_train[j], output)

                # à ce stade, output contient la sortie du réseau de neurones
                # on va donc calculer l'erreur de la dernière couche

                # propagation en arrière pour chaque échantillon dans tous les layers (en commençant par la dernière couche)
                error = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)

            # calculate average error on all samples
            err /= samples
            print('epoch %d/%d   error=%f' % (i+1, epochs, err))