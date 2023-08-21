quote = "success is no accedient. It is hard work, perservrance, learning, studing, sacrifice and most of all, love of what you are doing or learning to do"

prep = {"as", "but", "by", "for", "in", "of", "an", "to", "with"}


def find_prep(custom_quote, custom_prep):
    my_set = set(custom_quote.split(" "))
    finded_preps_set = my_set.intersection(custom_prep)
    return finded_preps_set


print(find_prep(quote, prep))
