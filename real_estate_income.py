import argparse
from datetime import datetime
from typing import List, Optional


def months_between(start: datetime, end: datetime) -> int:
    """Return number of calendar months between two dates inclusive."""
    return (end.year - start.year) * 12 + end.month - start.month + 1


def calculate_income(
    start: datetime,
    end: datetime,
    rent_per_tenant: float,
    maintenance_cost: float,
    vacancy_rate: float,
    tax_rate: float,
    occupancy: Optional[List[float]] = None,
) -> float:
    """Calculate expected net income from a rental apartment.

    Parameters
    ----------
    start : datetime
        Start date of calculation period.
    end : datetime
        End date of calculation period.
    rent_per_tenant : float
        Monthly rent when fully occupied.
    maintenance_cost : float
        Monthly maintenance costs.
    vacancy_rate : float
        Expected vacancy rate as a fraction (e.g. 0.1 for 10%).
    tax_rate : float
        Tax percentage applied to income after maintenance (e.g. 0.2 for 20%).
    occupancy : Optional[List[float]]
        Optional list specifying occupancy fraction for each month. If not
        provided, ``vacancy_rate`` is used to compute a constant occupancy.

    Returns
    -------
    float
        Net income for the period after maintenance and taxes.
    """
    months = months_between(start, end)
    if occupancy is not None:
        if len(occupancy) != months:
            raise ValueError("Occupancy list length must match number of months")
        occupancy_list = occupancy
    else:
        occupancy_list = [1.0 - vacancy_rate] * months

    gross_income = sum(rent_per_tenant * occ for occ in occupancy_list)
    maintenance_total = maintenance_cost * months
    taxable_income = gross_income - maintenance_total
    taxes = taxable_income * tax_rate
    net_income = taxable_income - taxes
    return net_income


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real estate income calculator")
    parser.add_argument("start", help="start date YYYY-MM-DD")
    parser.add_argument("end", help="end date YYYY-MM-DD")
    parser.add_argument("rent", type=float, help="monthly rent when occupied")
    parser.add_argument("maintenance", type=float, help="monthly maintenance cost")
    parser.add_argument("vacancy", type=float, help="vacancy rate (0-1)")
    parser.add_argument("tax", type=float, help="tax rate (0-1)")
    args = parser.parse_args()

    start = datetime.fromisoformat(args.start)
    end = datetime.fromisoformat(args.end)
    income = calculate_income(
        start,
        end,
        args.rent,
        args.maintenance,
        args.vacancy,
        args.tax,
    )
    print(f"Net income from {start.date()} to {end.date()}: {income:.2f}")
