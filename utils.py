# Utility Functions for Validation and Formatting

def validate_email(email):
    """Validate the email format."""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$'
    if re.match(pattern, email):
        return True
    return False


def format_date(date_obj):
    """Format a date object to YYYY-MM-DD format."""
    return date_obj.strftime('%Y-%m-%d')


def format_currency(amount):
    """Format a number as currency."""
    return f'${amount:,.2f}'
