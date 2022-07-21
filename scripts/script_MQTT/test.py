#================================================================

# this = {'rabbit' : '1', 'habbit' : '2'}

# __statement = ""
# for ix in this:
#     #print(ix)
#     #print(this[ix])

#     __statement += f" '{ix}' = {this[ix]},"
#     __statement = __statement[:-1]
#     print(__statement)

#================================================================

# error = {'trigger' : False, 'value' : 0, 'msg' : ''}
# print(error['value'])


#================================================================


# mylist = {"a" : "aaa", "b" : "bbb", "c" : "ccc"}
# newlist = {}

# mylist.update(newlist)
# # for iz in newlist:
# #     mylist.update()

# print(mylist)

#.......................... Outside imports  .........................
import sys
sys.path.append('D:\Python\Monitoring Scripts\SilentPython 2')  
import lib.sqlight as sqlight

def main(sql_client=sqlight.client,appname="", property={}):
    print("hello world")

