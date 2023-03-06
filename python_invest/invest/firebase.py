def parser(data: list[dict]) -> list:
    try:
        result = []
        for value in data:
            fields = list(value['mapValue']['fields'].keys())
            # TODO: handle non-string values or nested objects
            values = [
                value['mapValue']['fields'][key]['stringValue']
                for key in fields
            ]
            result.append(dict(zip(fields, values)))
        return result
    except Exception as er:
        raise ValueError(f'firebase parser failure. Detail {er}') from er
