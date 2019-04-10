#!/usr/bin/env python3
import os
import urllib.request
from flask import Flask

from .parser import from_html_string


app = Flask(__name__)


COUNTER_TYPES = [
    'Correted',
    'Uncorrectables',
]
"""Define counter type bits of data"""
# Ref: https://prometheus.io/docs/instrumenting/writing_exporters/


def clean_address(address):
    return address.replace('.', '_')


@app.route('/<prefix>/<address>')
def prometheus(prefix, address):
    url = f'http://{address}/cgi-bin/status'
    with urllib.request.urlopen(url) as response:
        doc_contents = response.read()

    data = from_html_string(doc_contents)
    response = []

    # Clean up the address so Prometheus can parse it
    address = clean_address(address)

    for ch in data['DownstreamBondedChannels']:
        for numeric in [
                'ChannelID',
                'Corrected',
                'Frequency',
                'Power',
                'SNR',
                'Uncorrectables',
                ]:
            response.append(
                '{prefix}_{address}_downstream_ch{ch}_{name} {val} '.format(
                    prefix=prefix,
                    address=address,
                    ch=str(int(ch["Channel"])),
                    name=numeric.lower()
                    + '_total' if numeric in COUNTER_TYPES else '',
                    val=ch[numeric],
                ))

    response.append(
        '{prefix}_{address}_downstream_channel_count {val}'.format(
            prefix=prefix,
            address=address,
            val=len(data['DownstreamBondedChannels']),
        )
    )

    for ch in data['UpstreamBondedChannels']:
        for numeric in [
                'ChannelID',
                'Frequency',
                'Power',
                'SymbolRate',
                ]:
            response.append(
                '{prefix}_{address}_upstream_ch{ch}_{name} {val} '.format(
                    prefix=prefix,
                    address=address,
                    ch=str(int(ch["Channel"])),
                    name=numeric.lower(),
                    val=ch[numeric],
                ))

    response.append(
        '{prefix}_{address}_upstream_channel_count {val}'.format(
            prefix=prefix,
            address=address,
            val=len(data['UpstreamBondedChannels']),
        )
    )

    return '\n'.join(response)


def main():
    app.run(
        host=os.environ.get('FLASK_HOST', '0.0.0.0'),
        port=int(os.environ.get('FLASK_PORT', 5000)))


if __name__ == '__main__':
    main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
