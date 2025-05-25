def calculate_monthly_payment(principal_amount: float, annual_interest_rate: float, loan_term_years: int) -> float:
    """Calculates the monthly payment for a loan.

    Args:
        principal_amount: The total amount of the loan.
        annual_interest_rate: The annual interest rate (e.g., 5 for 5%).
        loan_term_years: The term of the loan in years.

    Returns:
        The calculated monthly payment amount.
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    number_of_payments = loan_term_years * 12

    if principal_amount < 0:
        raise ValueError("Principal amount cannot be negative.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if loan_term_years <= 0:
        raise ValueError("Loan term must be greater than zero years.")

    if monthly_interest_rate == 0:  # Handle zero interest rate case
        if number_of_payments == 0: # This case is now prevented by loan_term_years > 0 validation
             return principal_amount # Or arguably an error, but problem implies calculation
        return principal_amount / number_of_payments

    # Standard formula for monthly payment
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    numerator = principal_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** number_of_payments)
    denominator = ((1 + monthly_interest_rate) ** number_of_payments) - 1
    
    # Denominator being zero is highly unlikely with positive interest rate and term,
    # as (1+i)^n would be > 1. If principal is 0, payment is 0.
    if denominator == 0:
        if principal_amount == 0:
            return 0.0
        # This path should ideally not be reached if inputs are valid (i>0, n>0)
        # Consider raising an error for unexpected mathematical results if truly hit.
        # For now, assuming valid loan scenarios where this doesn't cause issues.
        # Based on previous logic, this condition was determined to be improbable.
        # However, if it were to happen, it implies an issue not covered by typical loan math.
        # A very small i and large n or vice-versa might lead to precision issues,
        # but not typically a zero denominator if i > 0.
        # If we are here, and P > 0, it implies an issue.
        # Given the problem scope, we assume standard calculations apply.
        # However, if for some reason (1+i)^n IS 1 (and i > 0), it's problematic.
        # This should not happen for real i > 0 and integer n > 0.
        # Let's rely on the function's inputs being validated before this point.
        # If principal_amount is 0, the numerator is 0, so payment is 0.
        # If monthly_interest_rate is positive, (1+monthly_interest_rate) is > 1.
        # If number_of_payments is positive, (1+monthly_interest_rate)^number_of_payments is > 1.
        # So denominator = ((1+monthly_interest_rate)^number_of_payments) - 1 is > 0.
        # Thus, no division by zero if interest rate > 0 and term > 0.
        pass


    monthly_payment = numerator / denominator
    return monthly_payment

if __name__ == "__main__":
    def get_positive_float_input(prompt: str) -> float:
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Value must be a positive number. Please try again.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_positive_int_input(prompt: str) -> int:
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Value must be a positive integer. Please try again.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    print("Loan Payment Calculator")
    print("-----------------------")

    try:
        principal = get_positive_float_input("Enter principal loan amount (BHD): ")
        annual_rate = get_positive_float_input("Enter annual interest rate (e.g., 5 for 5%): ")
        term_years = get_positive_int_input("Enter loan term in years: ")

        monthly_payment_amount = calculate_monthly_payment(principal, annual_rate, term_years)
        print(f"Your estimated monthly payment is: {monthly_payment_amount:.3f} BHD")

    except ValueError as e:
        # This will catch validation errors raised from calculate_monthly_payment
        # if we decide to make its internal checks raise errors.
        # Currently, input functions handle positive checks, and calculate_monthly_payment assumes valid inputs.
        # Let's add specific checks in calculate_monthly_payment for negative values and zero term.
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
