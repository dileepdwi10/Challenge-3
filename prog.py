import json
import argparse
############################################################################################################
# Save this code as prog.py and run it like this:
# python prog.py -k x/y/z -o '{"x":{"y":{"z":"a"}}}'
# python prog.py -k a/b/c -o '{"a":{"b":{"c":"d"}}}'
############################################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--object", help="JSON object as input")
parser.add_argument("-k", "--key", help="Key to serach in input object")
args = parser.parse_args()
object = args.object
key=args.key

try:
    jsonObject = json.loads(object)
except:
    print("Invalid json object")
    exit(-1)

def findKeyInJson(key, json):
    keyPath=key.split('/')
    for k in keyPath:
        try:
            json  = json[k]
            result = json
        except:
            result = "Not found!"
            break
    return result
#
if __name__ == "__main__":
    result = findKeyInJson(key, jsonObject)
    print("Object:", jsonObject)
    print("Key:", key)
    print("Result:", result)
