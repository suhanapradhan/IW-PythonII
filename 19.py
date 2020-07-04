class parent:
   def check(self, str1):
        lists= []
        parenthesis= {"(": ")", "{": "}", "[": "]"}
        for p in str1:
            if p in parenthesis:
                lists.append(p)
            elif len(lists) == 0 or parenthesis[lists.pop()] != p:
                return False
        return len(lists) == 0

print(parent().check("(){}[]"))
print(parent().check("()[{)}"))
