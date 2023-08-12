def month_twelve_revenue(allocations):
    # Initial values
    total_customer_count = 1000
    organic_growth = 25
    baseline_monthly_revenue_per_customer = 100

    # Role-related values
    new_business_acquisition_rate = 5
    account_manager_rate = 0.25
    account_manager_capacity = 25
    account_manager_churn_reduction = 0.05
    churn_reduction_per_csat = 0.15

    for month in allocations:
        # Extract current month allocation
        support = month[0]
        account_manager = month[1]
        acquisition = month[2]

        # Update churn rates based on employee allocation
        unmanaged_customer_churn = 0.10  # baseline churn
        for _ in range(support):
            # Reduce relative churn by 15% for each additional CSAT percentage point
            unmanaged_customer_churn = unmanaged_customer_churn - (
                unmanaged_customer_churn * churn_reduction_per_csat
            )
        # Reduce relative churn by 5% for managed customers
        managed_customer_churn = unmanaged_customer_churn - (
            unmanaged_customer_churn * account_manager_churn_reduction
        )

        # Calculate acquired customers based on number of New Business Acquisition
        acquired_customers = acquisition * new_business_acquisition_rate
        total_customer_count = (
            total_customer_count + organic_growth + acquired_customers
        )

        # Calculate number of managed and unmanaged customers based on number of Account Manager
        managed_customer_count = account_manager * account_manager_capacity
        unmanaged_customer_count = total_customer_count - managed_customer_count

        # Subtract churned customers
        managed_customer_count -= int(managed_customer_count * managed_customer_churn)
        unmanaged_customer_count -= int(
            unmanaged_customer_count * unmanaged_customer_churn
        )
        total_customer_count = managed_customer_count + unmanaged_customer_count

        # Calculate revenue
        managed_revenue = managed_customer_count * (
            baseline_monthly_revenue_per_customer * (1 + account_manager_rate)
        )
        unmanaged_revenue = (
            unmanaged_customer_count * baseline_monthly_revenue_per_customer
        )
        total_revenue = managed_revenue + unmanaged_revenue

    return total_revenue


# 121525.0
# allocations = [
#     [8, 3, 9],
#     [10, 0, 10],
#     [8, 4, 8],
#     [8, 12, 0],
#     [5, 10, 5],
#     [5, 7, 8],
#     [15, 1, 4],
#     [11, 5, 4],
#     [1, 2, 17],
#     [3, 15, 2],
#     [0, 0, 20],
#     [6, 8, 6],
# ]

# 122475.0
# allocations = [
#     [6, 12, 2],
#     [17, 1, 2],
#     [12, 0, 8],
#     [3, 13, 4],
#     [15, 4, 1],
#     [10, 5, 5],
#     [14, 1, 5],
#     [8, 3, 9],
#     [9, 1, 10],
#     [20, 0, 0],
#     [2, 15, 3],
#     [2, 2, 16],
# ]

# 128800.0
# allocations = [
#     [7, 1, 12],
#     [16, 1, 3],
#     [15, 2, 3],
#     [5, 14, 1],
#     [9, 5, 6],
#     [7, 1, 12],
#     [2, 0, 18],
#     [8, 7, 5],
#     [2, 12, 6],
#     [2, 2, 16],
#     [8, 1, 11],
#     [11, 0, 9],
# ]

# print(month_twelve_revenue(allocations))
