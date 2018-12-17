# -*- coding: UTF-8 -*-
# 有两种算法。一种是Trie一种是栈模拟。

class Trie:
    def __init__(self):
        self.path = {}
        self.value = [0]
        self.sequence = -1
    def __addstack__(self, stack, sequence = -1):
        if sequence == -1:
            sequence = self.sequence + 1

        head = stack[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(stack) > 1:
            remains = stack[1:]
            node.__addstack__(remains, sequence)

        if sequence - self.sequence > 1 and max(self.value) != 0:
            node.value.append(1)
        else:
            node.value[-1] += 1

        self.sequence = sequence

    def __printcount__(self,  count):
        child_indexes = self.path.keys()
        for child_index in child_indexes:
            print("(%s, %s)" % (child_index, self.path[child_index].value))
            child = self.path[child_index]
            res = child.__printcount__(count)
            if res:
                return res
            if max(child.value) >= count:
                return child_index
        return None


def main(stacks):
    test = Trie()
    for stack in stacks:
        test.__addstack__(stack)
    print test.__printcount__(2)

if __name__=='__main__':
    stack1 = ['1','2','3','4','5']
    stack2 = ['1','2','3','4','5']
    stack3 = ['1','2','3','4','6']
    stack4 = ['1','2','3','7','8']
    stack5 = ['1','2','3','9','10']
    stack6 = ['1','2','3','9','11', '13']
    stack7 = ['1','2','3','9','12']
    stack8 = ['1','2','3','9','13']
    stack9 = ['1','2','3','9','14']

    test_stacks1 = [stack1, stack2, stack3, stack4, stack5,
            stack6, stack7, stack8, stack9]
    main(test_stacks1)

    stack10 = ['15','2','3','9','14']
    test_stacks2 = [stack1, stack2, stack3, stack4, stack5,
            stack6, stack7, stack8, stack9, stack10]
    main(test_stacks2)

    stack10 = ['1','2','3','9','14']
    test_stacks2 = [stack1, stack2, stack3, stack4, stack5,
            stack6, stack7, stack8, stack9, stack10]
    main(test_stacks2)



