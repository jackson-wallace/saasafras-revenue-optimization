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

    for i, month in enumerate(allocations):
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

        # print("-------------------------------------")
        # print(f"Month {i + 1}")
        # print("Total customers: ", total_customer_count)
        # print("Total revenue: ", total_revenue)
        # print("-------------------------------------")

    return total_revenue
