def calibrate_predictions(predictions, calibration_factor):
    """
    Calibrates model predictions using a calibration factor.

    Args:
        predictions (list or np.array): The raw predictions from the model.
        calibration_factor (float): The factor to adjust the predictions.

    Returns:
        list or np.array: The calibrated predictions.
    """
    return predictions * calibration_factor

def adjust_parameters(params, adjustment_factor):
    """
    Adjusts model parameters based on a given adjustment factor.

    Args:
        params (dict): A dictionary of model parameters.
        adjustment_factor (float): The factor to adjust the parameters.

    Returns:
        dict: The adjusted parameters.
    """
    return {key: value * adjustment_factor for key, value in params.items()}