# function to generate mobile number


def generate_number(country_code, provider_code, first_digits, last_digits):
    print(
        f"{country_code}",
        f"{provider_code}",
        f"{first_digits}",
        f"{last_digits}",
        sep="-",
    )


generate_number(
    country_code="+94", provider_code="70", first_digits="123", last_digits=3456
)
