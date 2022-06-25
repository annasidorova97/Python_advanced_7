from stack_class import Stack

brackets = input('Enter a sequence of brackets: ')
st = Stack()


def checking_a_sequence(sequence_of_brackets):
    for item in sequence_of_brackets:
        if item in '([{':
            st.push(item)
        elif item in ')]}':
            if st.isEmpty():
                return 'Несбалансированно'
            elif item == ')' and st.peek() == '(':
                st.pop()
            elif item == ']' and st.peek() == '[':
                st.pop()
            elif item == '}' and st.peek() == '{':
                st.pop()
            else:
                return 'Несбалансированно'
    if st.isEmpty():
        return 'Cбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(checking_a_sequence(brackets))





