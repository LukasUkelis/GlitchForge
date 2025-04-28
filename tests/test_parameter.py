from glitch_forge import parameter


def test_parameter_base():
    # Test the base parameter class
    param = parameter.Param(
        val=5,
        var_type=int,
        label="Test Parameter",
        min_val=0,
        max_val=10,
        tooltip="This is a test parameter",
        placeholder="Enter a value",
    )
    assert param.val == 5
    assert param.var_type is int
    assert param.label == "Test Parameter"
    assert param.min_val == 0
    assert param.max_val == 10
    assert param.tooltip == "This is a test parameter"
    assert param.placeholder == "Enter a value"
