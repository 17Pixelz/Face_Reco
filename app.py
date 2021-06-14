from recognizeFaces import detectFaces
from getImages import getAllImages

# Telecharger les images depuis FireBase et les stockees dans le repertoire ./img/unkown
getAllImages()

# Faire la recenaissance des visages et generer le fichier des abscences
detectFaces()