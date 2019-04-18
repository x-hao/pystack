if __name__ == '__main__':
    # 在 Python 3 中，/ 运算符总是表示浮点除法。
    # 列表可包含任何数据类型的元素，同一个列表中的元素无须为同一类型。下面的列表中就包含一个字符串、一个浮点数和一个整数。
    a = ['a']
    b = a + [2, 3]  # 运算符连接列表以创建一个新列表。列表可包含任何数量的元素；没有尺寸限制（除了可用内存的限制）
    b.append(['for'])  # 方法向列表的尾部添加一个新的元素
    b.append('fdk')
    for i in b:
        print(isinstance(i, int))
    # 列表是以类的形式实现的。“创建”列表实际上是将一个类实例化。因此，有多种方法可以操作列表。extend() 方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。
    b.extend(['True'])
    # 等等，什么？是这样的：如果没有在列表中找到该值， index()
    # 方法将会引发一个异常。这是
    # Python
    # 语言和其它多数语言的最显著区别，它们多半会返回一些无效的索引值（像是 - 1）。当然，刚开始这一点看起来比较讨厌，但我想你会逐渐欣赏它。这意味着您的程序将会在问题的源头处崩溃，而不是之后奇怪地、默默地崩溃。请记住， -1
    # 是合法的列表索引值。如果
    # index()
    # 方法返回 - 1，可能会导致调整过程变得不那么有趣！
    print(b.count('no'))
    print(b.index(['for']))

    print(b)
    del b[1]
    print(b)
    # 	你可以尽情地调用 remove() 方法，但如果试图删除列表中不存在的元素，它将引发一个异常。
    b.remove('fdk')
    print(b)

    # ①    无法向元组添加元素。元组没有
    # append()
    # 或
    # extend()
    # 方法。
    # ②    不能从元组中删除元素。元组没有
    # remove()
    # 或
    # pop()
    # 方法。
    # ③    可以
    # 在元组中查找元素，由于该操作不改变元组。
    # ④    还可以使用 in 运算符检查某元素是否存在于元组中。

    # 元组的速度比列表更快。如果定义了一系列常量值，而所需做的仅是对它进行遍历，那么请使用元组替代列表。
    # 对不需要改变的数据进行“写保护”将使得代码更加安全。使用元组替代列表就像是有一条隐含的
    # assert 语句显示该数据是常量，特别的想法（及特别的功能）必须重写。（？？）
    # 一些元组可用作字典键（特别是包含字符串、数值和其它元组这样的不可变数据的元组）。列表永远不能当做字典键使用，因为列表不是不可变的。

    # 元组可转换成列表，反之亦然。内建的 tuple() 函数接受一个列表参数，并返回一个包含同样元素的元组，而 list() 函数接受一个元组参数并返回一个列表。从效果上看， tuple() 冻结列表，而 list() 融化元组。

    v = (1, 2, 3)
    (x, y, z) = v
    print(x, y, z)

    s = {1, 2, 3, 4}
    b = ['3242', '3423', '33', '33']
    s = set(b)
    print(type(s))  # 只能包含简单数据类型？？？？
    print(b)
    # 有两种方法可向现有集合中添加值： add() 方法和 update() 方法。
    # 	discard() 接受一个单值作为参数，并从集合中删除该值。如果针对一个集合中不存在的值调用 discard() 方法，它不进行任何操作。不产生错误；只是一条空指令。
    # 区别在这里：如果该值不在集合中，remove() 方法引发一个 KeyError 例外。

    # 字典没有预定义的大小限制。可以随时向字典中添加新的键值对，或者修改现有键所关联的值。继续前面的例子：
    d = {'a': 'aa', 'b': 'cc'}
    print(d)

    print(None == None)
    print("----------------")
    # print(none == None)
    print("----------------")
