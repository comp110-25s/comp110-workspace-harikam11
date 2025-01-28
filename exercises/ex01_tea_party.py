"""Planning a Tea Party"""

__author__: str = "730765138"


def main_planner(guests: int) -> None:
    """Produces Printed Output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Number of Tea Bags Needed Based on Number of Guests"""
    return 2 * people


def treats(people: int) -> int:
    """Number of Treats Needed Based on Number of Tea Guests Drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of Tea Bags and Treats Combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending you tea party? ")))
