import numpy as np


def seq_array():
    data1 = range(1, 6)
    print(data1, type(data1))
    a1 = np.array(data1)
    print(a1, type(a1))

    data2 = [0.1, 5, 4, 12, 0.5]
    print(data2, type(data2))
    a2 = np.array(data2)
    print(a2, a2.dtype)
    print()


def td_array():
    a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a3.dtype, a3, sep='\n')
    print()
    a4 = np.arange(0, 10, 2)
    print(a4.dtype, a4)
    print()
    print("arange(12)")
    print(np.arange(12))
    print("shape")
    print(np.arange(12).shape)
    print()
    print("arange(12).reshape(4, 3)")
    print(np.arange(12).reshape(4, 3))
    print("shape")
    print(np.arange(12).reshape(4, 3).shape)
    print()
    print(np.linspace(1, 10, 10))


def num_array():
    print("np.zeros(10)")
    print(np.zeros(10))
    print()
    print("np.zeros((3, 4))")
    print(np.zeros((3, 4)))
    print()
    print("np.ones(5)")
    print(np.ones(5))
    print()
    print("np.ones((3, 5))")
    print(np.ones((3, 5)))
    print()
    print("np.eye(3)")
    print(np.eye(3))
    print()


def type_conversion():
    str_array = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
    print(str_array, str_array.dtype)
    float_array = str_array.astype(float)
    print(float_array, float_array.dtype)
    print()


def rand_array():
    r1 = np.random.rand(2, 3)
    print("np.random.rand(2,3)\n", r1)
    print()
    r2 = np.random.rand()
    print("np.random.rand()\n", r2)
    print()
    r3 = np.random.rand(2, 3, 4)
    print("np.random.rand(2, 3, 4)\n", r3)
    print()
    r4 = np.random.randint(10, size=(3, 4))
    print("np.random.randint(10, size=(3, 4))\n", r4)
    print()
    r5 = np.random.randint(1, 30)
    print("np.random.randint(1, 30)\n", r5)
    print()


def operation_array():
    o1 = np.array([10, 20, 30, 40])
    o2 = np.array([1, 2, 3, 4])
    print("o1 = {}, o2 = {}".format(o1, o2))
    print("o1+o2=", o1 + o2)
    print("o1-o2=", o1 - o2)
    print("o2*2=", o2 * 2)
    print("o2**2=", o2 ** 2)
    print("o1*o2=", o1 * o2)
    print("o1/o2=", o1 / o2)
    print("o1/(o2**2)=", o1 / (o2 ** 2))
    print("o1 > 20=", o1 > 20)  # 비교연산 가능
    print()


def statistics_array():
    s1 = np.arange(5)
    print("s1 = ", s1)
    print("s1.sum() = {}, s1.mean()= {}".format(s1.sum(), s1.mean()))
    print("s1.std() = {}, s1.var() = {}".format(s1.std(), s1.var()))
    print("s1.max() = {}, s1.min() = {}".format(s1.max(), s1.min()))
    print()
    s2 = np.arange(1, 5)
    print("s2 = ", s2)
    print("s2.cumsum() =", s2.cumsum())
    print("s2.cumprod() =", s2.cumprod())
    print()


def operation_mat():
    A = np.array([0, 1, 2, 3]).reshape(2, 2)
    print("A = \n", A)
    B = np.array([3, 2, 0, 1]).reshape(2, 2)
    print("B = \n", B)

    print("A.dot(B) = \n", A.dot(B))
    print("np.dot(A, B) = \n", np.dot(A, B))
    print("np.transpose(A) =\n", np.transpose(A))
    print("A.transpose() =\n", A.transpose())
    print("np.linalg.inv(A) =\n", np.linalg.inv(A))
    print("np.linalg.det(A) =\n", np.linalg.det(A))
    print()


def indexing_slicing():
    a1 = np.array([0, 10, 20, 30, 40, 50])
    print("a1 =", a1)
    print("a1[[1, 3, 4]]=", a1[[1, 3, 4]])
    print("a1[a1 > 3]", a1[a1 > 30])
    print("a1[(a1 % 20) == 0]", a1[(a1 % 20) == 0])
    a2 = np.arange(10, 100, 10).reshape(3, 3)
    print("a2 =\n", a2)
    print("a2[[0,2], [0,1]] =", a2[[0, 2], [0, 1]])  # [행1, 행2, ...] [열1, 열2, ...]
    print()
    b1 = np.array([0, 10, 20, 30, 40, 50])
    print("b1 =", b1)
    print("b1[1:4] =", b1[1:4])
    print("b1[:3] =", b1[:3])
    b1[2:5] = np.array([25, 35, 45])
    print("b1 =", b1)
    b1[3:] = 60
    print("b1 =", b1)
    b2 = np.arange(10, 100, 10).reshape(3, 3)
    print("b2 = \n", b2)
    print("b2[1:3, 1:3] = \n", b2[1:3, 1:3])
    print("b2[:3, 1:] = \n", b2[:3, 1:])
    print("b2[1][:2] = \n", b2[1][:2])
    b2[0:2, 1:3] = ([[25, 35], [55, 65]])
    print("b2 =\n", b2)

if __name__ == "__main__":
    seq_array()
    td_array()
    num_array()
    type_conversion()
    rand_array()
    operation_array()
    statistics_array()
    operation_mat()
    indexing_slicing()
