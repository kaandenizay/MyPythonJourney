# area = 0
#
#
# def area_of_square(length: float):
#     global area
#     area = length * length
#
#
# area_of_square(30)
# print(f'The area is {area}')

"""
Actually, most of the time we don't want to update global variable inside
the scope, its very rarely possible and always think twice before doing this usage
"""


def area_of_square(length: float) -> float:
    return length * length


if __name__ == '__main__':
    """
    This __name__ equals main if its run inside this module,
    Outside of this module, when imported,  its not run 
    """
    area = area_of_square(30)
    print(f'The area is {area}')

    print(f'in better_code.py, __name__ is {__name__}')
