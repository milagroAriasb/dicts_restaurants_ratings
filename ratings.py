"""Restaurant rating lister."""

my_file = open ("scores.txt")
restaurants = {}

def restaurant_ratings(my_file):
   

    for line in my_file:
        line =  line.rstrip()
        word = line.split(":")

        restaurant_name = word[0]
        rating = word[1]
        restaurants[restaurant_name] = rating
    #print restaurants    
        
    #for list_name_rest in restaurants.keys():
     #   print "{}".format(list_name_rest)

    #order_name_rest = [list_name_rest for list_name_rest in restaurants.keys()]
    #sorted_name_rest =  sorted(order_name_rest) 
    #print sorted_name_rest

    # i = 0
    # while i < len(sorted_name_rest):
    #     print sorted_name_rest[i], restaurants[sorted_name_rest[i]]
    #     i = i + 1
    


    # for sorted_name_rest, scores in sorted(restaurants.items()):
    #     print "{} : {}".format(sorted_name_rest, scores)
    #print_restaurants(restaurants)    





    # for sorted_name_rest, scores in sorted(restaurants.items()):
    #     print "{} : {}".format(sorted_name_rest, scores)

    print_restaurants(restaurants) 
    add_restaurant()
    print_restaurants(restaurants) 



def print_restaurants(restaurants):


    for sorted_name_rest, scores in sorted(restaurants.items()):
        print "{} : {}".format(sorted_name_rest, scores)




def add_restaurant():
   
    new_restaurant = raw_input("what's the name of restaurant? ")
    score_restaurant = int(raw_input("what's the score? "))
    restaurants[new_restaurant] = score_restaurant






restaurant_ratings(my_file)









