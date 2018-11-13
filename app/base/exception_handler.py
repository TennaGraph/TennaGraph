# Pip imports
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler
from rest_framework.settings import api_settings


def base_exception_handler(exc, context):
    # Call DRF's default exception handler first,
    # to get the standard error response.

    response = exception_handler(exc, context)
    errors = {}

    # check that a DRFValidationError exception is raised
    if isinstance(exc, DRFValidationError):
        # here prepare the 'custom_error_response' and
        # set the custom response data on response object
        errors["errors"] = construct_validation_error_response(exc, response)

    if response:
        response.data = errors
    return response


def construct_validation_error_response(exc, response):
    if isinstance(exc.detail, list):
        def_key = getattr(api_settings, "NON_FIELD_ERRORS_KEY", "none")
        return {def_key: response.data}
    return response.data
