__all__ = ['get_data']

import os
import json
import pandas as pd

pd.options.mode.chained_assignment = None


def get_data(time_frame: str) -> tuple[dict, pd.DataFrame]:

    time_frame = time_frame.capitalize()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{base_dir}/data/crypto{time_frame}.json') as f:
        expected_asdict = json.load(f)

    __raw_df = pd.DataFrame(expected_asdict)
    expected_asdf = __raw_df[
        [
            'last_close',
            'last_open',
            'last_max',
            'last_min',
            'volumeRaw',
            'change_precent',
        ]
    ]
    expected_asdf.rename(
        columns={
            'last_close': 'Price',
            'last_open': 'Open',
            'last_max': 'High',
            'last_min': 'Low',
            'volumeRaw': 'Vol',
            'change_precent': 'Change',
        },
        inplace=True,
    )
    expected_asdf['Date'] = pd.to_datetime(
        pd.to_datetime(__raw_df.rowDateTimestamp)
    ).dt.strftime('%m/%d/%Y')
    expected_asdf.sort_values('Date', inplace=True)
    return expected_asdict, expected_asdf
