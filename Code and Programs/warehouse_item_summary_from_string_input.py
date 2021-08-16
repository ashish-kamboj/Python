"""
Code to get the summary of items present in the warehouse. Transactions log store the quantity of items 
brought-in to the warehouse and how many items were taken out of the warehouse.

Transaction log is stored in the string format.
"""


transactionLog = """
Item1   10  
Item2 	  1    
Item1         -5          
Item3     40        
Item2    -1      
"""


def stringParse(transactionLog):

    item_list = transactionLog.split(sep='\n')
    item_list = list(filter(None, item_list))

    yield from item_list


def itemSummary(func):

    summary_dict = {}

    for item in func:
        new_list = item.split(sep=None)

        if(new_list[0] not in summary_dict):
            summary_dict[new_list[0]] = new_list[1]
        else:
            sum = int(summary_dict[new_list[0]]) + int(new_list[1])
            summary_dict[new_list[0]] = sum

    return summary_dict


summary = itemSummary(stringParse(transactionLog))
print(summary)

