# kg_sujaylokesh_2020
 Kargo assignment

Question:
Determine whether a one-to-one character mapping exists from one string, s1, to another string,
s2.

For example, given s1 = abc and s2 = bcd, print "true" into stdout since we can map each
character in "abc" to a character in "bcd".

Given s1 = foo and s2 = bar, print "false" since the character ‘o’ cannot map to two characters.

But given s1 = bar and s2 = foo, print "true" since each character in "bar" can be mapped to a
character in "foo".

Approaches : 

        Approach 1 : Find if s1 contains unique characters.
                        If s1 has only unique characters:
                            print True
                        else if characters are repeated: 
                            print False
        Approach 2 : Create dictionary for s1 -> s2 mapping
                     Reverse the dictionary
                     key is s2 and value is a list of mappings in s1
                     (ex: 1:[2,3],2:[1])
                     Then count the number of values in the list
                     if count > 1:
                        print False
                    else:
                        print True