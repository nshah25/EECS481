import ast
import astor
import sys
import random
import pprint
import copy


class myVisitor(ast.NodeVisitor):
    def __init__(self):
        self.counter = 0

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            self.counter += 1
            print("Visiting Add, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.op, ast.Sub):
            self.counter += 1
            print("Visiting Sub, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.op, ast.Mult):
            self.counter += 1
            print("Visiting Mult, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.op, ast.FloorDiv):
            self.counter += 1
            print("Visiting Div, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.op, ast.BitOr):
            self.counter += 1
            print("Visiting BitOr, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.op, ast.BitAnd):
            self.counter += 1
            print("Visiting BitAnd, counter = {}".format(self.counter))
            return self.generic_visit(node)

    def visit_BoolOp(self, node):

        if isinstance(node.op, ast.And):
            self.counter += 1
            print("Visiting And, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.op, ast.Or):
            self.counter += 1
            print("Visiting Or, counter = {}".format(self.counter))
            return self.generic_visit(node)

    def visit_Compare(self, node):
        if isinstance(node.ops[0], ast.Lt):
            self.counter += 1
            print("Visiting lt, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.ops[0], ast.Gt):
            self.counter += 1
            print("Visiting gt, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.ops[0], ast.LtE):
            self.counter += 1
            print("Visiting ltE, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.ops[0], ast.GtE):
            self.counter += 1
            print("Visiting gtE, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.ops[0], ast.Eq):
            self.counter += 1
            print("Visiting Equal, counter = {}".format(self.counter))
            return self.generic_visit(node)

        if isinstance(node.ops[0], ast.NotEq):
            self.counter += 1
            print("Visiting Not Equal, counter = {}".format(self.counter))
            return self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node, ast.Assign):
            # self.counter += 1
            print("Visiting Assign, counter = {}".format(self.counter))
            return self.generic_visit(node)
        
        
    def visit_Expr(self, node):
        if isinstance(node.value, ast.Call):
            # self.counter += 1
            print("Visiting Call, counter = {}".format(self.counter))
            return self.generic_visit(node)



class myTransformer(ast.NodeTransformer):
    def __init__(self, nodeToMutate):
        self.counter = 0
        self.nodeToMutate = nodeToMutate

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right
                new_node.op = ast.Sub()
                print("Changing Add {} counter to sub".format(self.counter))
                return ast.copy_location(new_node, node)

            print("Visiting Add, counter = {}".format(self.counter))

        if isinstance(node.op, ast.Sub):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right
                new_node.op = ast.Add()
                print("Changing Sub {} counter to add".format(self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.op, ast.FloorDiv):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right
                new_node.op = ast.Mult()
                print("Changing Div {} counter to Mult".format(self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.op, ast.Mult):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right
                new_node.op = ast.FloorDiv()
                print("Changing Mult {} counter to Div".format(self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.op, ast.BitOr):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right
                new_node.op = ast.BitXor()
                print("Changing BitOr {} counter to BitXor".format(self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.op, ast.BitAnd):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right
                new_node.op = ast.BitOr()
                print("Changing BitAnd {} counter to BitOr".format(self.counter))
                return ast.copy_location(new_node, node)

        return self.generic_visit(node)

    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BoolOp()
                new_node.op = ast.Or()
                new_node.values = node.values
                print("Changing And {} counter to Or".format(self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.op, ast.Or):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.BoolOp()
                new_node.op = ast.And()
                new_node.values = node.values
                print("Changing Or {} counter to And".format(self.counter))
                return ast.copy_location(new_node, node)
        return self.generic_visit(node)

    def visit_compare(self, node):
        if isinstance(node.ops[0], ast.Eq):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.ops[0] = ast.NotEq()
                print("Changing Equal {} counter to Not Equal".format(self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.ops[0], ast.NotEq):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.ops[0] = ast.Eq()
                print("Changing Not Equal {} counter to Equal".format(self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.ops[0], ast.Lt):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.ops[0] = ast.GtE()
                print("Changing Less than {} counter to Greater than or equal".format(
                    self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.ops[0], ast.LtE):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.op = ast.Gt()
                print("Changing Less than or Equal {} counter to Greater than".format(
                    self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.ops[0], ast.Gt):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.ops[0] = ast.LtE()
                print("Changing Greater than {} counter to Less than or equal".format(
                    self.counter))
                return ast.copy_location(new_node, node)

        if isinstance(node.ops[0], ast.GtE):
            self.counter += 1
            if(self.counter == nodeToMutate):
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.ops[0] = ast.Lt()
                print("Changing Greater than or equal {} counter to Less than".format(
                    self.counter))
                return ast.copy_location(new_node, node)
        return self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node, ast.Assign):
            self.counter += 1
            if(self.counter == nodeToMutate):
                print("Changing Assign RHS {} counter to 1".format(self.counter))
                new_node = ast.Pass()
                return ast.copy_location(new_node, node)
        return self.generic_visit(node)
    
    def visit_Expr(self, node):         
        if isinstance(node.value, ast.Call):
            self.counter += 1
            if(self.counter == nodeToMutate):
                print("Changing Call Function {} counter to 1".format(self.counter))
                new_node = ast.Pass()
                return ast.copy_location(new_node, node)
        return self.generic_visit(node)


initalTree = None
with open("./" + sys.argv[1]) as f:
    source = f.read()
    initalTree = ast.parse(source)

random.seed(666)
outputNum = sys.argv[2]
for i in range(int(outputNum)):
    # Code to make the files
    myTree = copy.deepcopy(initalTree)
    # myTree = initalTree

    myVistedTree = myVisitor()
    myVistedTree.visit(myTree)

    nodeToMutate = random.randint(1, myVistedTree.counter)

    myTransformedNode = myTransformer(nodeToMutate)
    myTransformedNode.visit(myTree)

    # Will now mutate 2 times
    nodeToMutate = random.randint(1, myVistedTree.counter)

    myTransformedNode = myTransformer(nodeToMutate)
    myTransformedNode.visit(myTree)

    fileWrite = open(str(i) + ".py", "w")
    fileWrite.write(str(astor.to_source(myTree)))
    fileWrite.close()


# myVistedTree = myVisitor()
# myVistedTree.visit(myTree)
# nodeToMutate = random.randint(1, myVistedTree.counter)
# myTransformedNode = myTransformer(nodeToMutate)
# myTransformedNode.visit(myTree)
# print( astor.to_source(myTree ))