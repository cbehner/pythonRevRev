def revrev(to_rev):
    st = list()

    # Go through sentence and push characters to list (stack) until it hits a space.
    for i in range(len(to_rev)):
        if to_rev[i] != " ":
            st.append(to_rev[i])

        # When a space is encountered print stack last letter first and then remove it from list
        else:
            while len(st) > 0:
                print(st[-1], end="")
                st.pop()
            print(end=" ")

    # Last word probably won't have space after it
    while len(st) > 0:
        print(st[-1], end="")
        st.pop()



if __name__ == '__main__':
    revrev('The quick brown fox')

