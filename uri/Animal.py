ani1 = input()
ani2 = input()
ani3 = input()

if ani1 == 'vertebrado' and ani2 == 'ave' and ani3 == 'carnivoro':
    animal = 'aguia'
if ani1 == 'vertebrado' and ani2 == 'ave' and ani3 == 'onivoro':
    animal = 'pomba'
if ani1 == 'vertebrado' and ani2 == 'mamifero' and ani3 == 'onivoro':
    animal = 'homem'

if ani1 == 'vertebrado' and ani2 == 'mamifero' and ani3 == 'herbivoro':
    animal = 'vaca'

if ani1 == 'invertebrado' and ani2 == 'inseto' and ani3 == 'hematofago':
    animal = 'pulga'

if ani1 == 'invertebrado' and ani2 == 'inseto' and ani3 == 'herbivoro':
    animal = 'lagarta'

if ani1 == 'invertebrado' and ani2 == 'anelideo' and ani3 == 'hematofago':
    animal = 'sanguessuga'

if ani1 == 'invertebrado' and ani2 == 'anelideo' and ani3 == 'onivoro':
    animal = 'minhoca'

print(animal)