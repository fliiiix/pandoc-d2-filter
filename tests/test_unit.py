from pandoc_d2_filter import d2


def test_call_d2_create_para_object(mocker):
    mocker.patch("os.path.isfile", return_value=False)
    mock = mocker.patch("subprocess.check_call")

    ret = d2(key="CodeBlock", value=[["", ["d2"], []], ""], format=None, meta={})

    assert isinstance(ret, dict)
    assert "t" in ret.keys()
    assert ret["t"] == "Para"

    mock.assert_called_once()
