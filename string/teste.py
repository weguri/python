class String(str):
    def __init__(self, val) -> None:
        self.val = val
        self.len_val = len(val)


obj = String("Frase: em para em teste de em ultima")


print(obj.split('em'))
print(obj.split('em')[-1])

print(len(obj.split('em')[-1]))
