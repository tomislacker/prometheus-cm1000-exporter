# arris-parser

## About
[![Build Status](https://travis-ci.org/tomislacker/prometheus-arris-exporter.svg?branch=master)](https://travis-ci.org/tomislacker/prometheus-arris-exporter)
[![](https://images.microbadger.com/badges/image/tomislacker/arris-parser.svg)](https://microbadger.com/images/tomislacker/arris-parser "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/tomislacker/arris-parser.svg)](https://microbadger.com/images/tomislacker/arris-parser "Get your own version badge on microbadger.com")

This project was created because my ISP locks down SNMP on my
[Arris SB6190](https://www.arris.com/surfboard/products/cable-modems/sb6190/)
though I still wanted to get this data into
[Prometheus](https://prometheus.io/). Keep in mind this
is my first exporter, so be nice.

## Example
1. Start the service via Docker
    ```sh
    $ docker run \
        -it \
        --rm \
        -p 54321:5000 \
        tomislacker/arris-parser:latest
    ```
1. Query it

    ```sh
    $ curl -s http://localhost:54321/modem/192.168.100.1
    ```

### Output
```
modem_192.168.100.1_downstream_ch1_channelid 17.0
modem_192.168.100.1_downstream_ch1_corrected 1056.0
modem_192.168.100.1_downstream_ch1_frequency 585.0
modem_192.168.100.1_downstream_ch1_power 1.7
modem_192.168.100.1_downstream_ch1_snr 40.95
modem_192.168.100.1_downstream_ch1_uncorrectables 26626.0
modem_192.168.100.1_downstream_ch2_channelid 2.0
modem_192.168.100.1_downstream_ch2_corrected 2230.0
modem_192.168.100.1_downstream_ch2_frequency 495.0
modem_192.168.100.1_downstream_ch2_power 0.4
modem_192.168.100.1_downstream_ch2_snr 40.37
modem_192.168.100.1_downstream_ch2_uncorrectables 14212.0
modem_192.168.100.1_downstream_ch3_channelid 3.0
modem_192.168.100.1_downstream_ch3_corrected 1691.0
modem_192.168.100.1_downstream_ch3_frequency 501.0
modem_192.168.100.1_downstream_ch3_power 0.6
modem_192.168.100.1_downstream_ch3_snr 40.37
modem_192.168.100.1_downstream_ch3_uncorrectables 15090.0
modem_192.168.100.1_downstream_ch4_channelid 4.0
modem_192.168.100.1_downstream_ch4_corrected 1778.0
modem_192.168.100.1_downstream_ch4_frequency 507.0
modem_192.168.100.1_downstream_ch4_power 1.2
modem_192.168.100.1_downstream_ch4_snr 40.37
modem_192.168.100.1_downstream_ch4_uncorrectables 14977.0
modem_192.168.100.1_downstream_ch5_channelid 5.0
modem_192.168.100.1_downstream_ch5_corrected 1493.0
modem_192.168.100.1_downstream_ch5_frequency 513.0
modem_192.168.100.1_downstream_ch5_power 1.3
modem_192.168.100.1_downstream_ch5_snr 40.37
modem_192.168.100.1_downstream_ch5_uncorrectables 15330.0
modem_192.168.100.1_downstream_ch6_channelid 6.0
modem_192.168.100.1_downstream_ch6_corrected 1899.0
modem_192.168.100.1_downstream_ch6_frequency 519.0
modem_192.168.100.1_downstream_ch6_power 1.6
modem_192.168.100.1_downstream_ch6_snr 40.37
modem_192.168.100.1_downstream_ch6_uncorrectables 18782.0
modem_192.168.100.1_downstream_ch7_channelid 7.0
modem_192.168.100.1_downstream_ch7_corrected 1533.0
modem_192.168.100.1_downstream_ch7_frequency 525.0
modem_192.168.100.1_downstream_ch7_power 1.8
modem_192.168.100.1_downstream_ch7_snr 40.95
modem_192.168.100.1_downstream_ch7_uncorrectables 7948.0
modem_192.168.100.1_downstream_ch8_channelid 8.0
modem_192.168.100.1_downstream_ch8_corrected 479.0
modem_192.168.100.1_downstream_ch8_frequency 531.0
modem_192.168.100.1_downstream_ch8_power 1.3
modem_192.168.100.1_downstream_ch8_snr 40.37
modem_192.168.100.1_downstream_ch8_uncorrectables 9120.0
modem_192.168.100.1_downstream_ch9_channelid 9.0
modem_192.168.100.1_downstream_ch9_corrected 1357.0
modem_192.168.100.1_downstream_ch9_frequency 537.0
modem_192.168.100.1_downstream_ch9_power 1.0
modem_192.168.100.1_downstream_ch9_snr 40.95
modem_192.168.100.1_downstream_ch9_uncorrectables 8143.0
modem_192.168.100.1_downstream_ch10_channelid 10.0
modem_192.168.100.1_downstream_ch10_corrected 1649.0
modem_192.168.100.1_downstream_ch10_frequency 543.0
modem_192.168.100.1_downstream_ch10_power 1.1
modem_192.168.100.1_downstream_ch10_snr 40.95
modem_192.168.100.1_downstream_ch10_uncorrectables 17168.0
modem_192.168.100.1_downstream_ch11_channelid 11.0
modem_192.168.100.1_downstream_ch11_corrected 777.0
modem_192.168.100.1_downstream_ch11_frequency 549.0
modem_192.168.100.1_downstream_ch11_power 1.2
modem_192.168.100.1_downstream_ch11_snr 40.37
modem_192.168.100.1_downstream_ch11_uncorrectables 13757.0
modem_192.168.100.1_downstream_ch12_channelid 12.0
modem_192.168.100.1_downstream_ch12_corrected 535.0
modem_192.168.100.1_downstream_ch12_frequency 555.0
modem_192.168.100.1_downstream_ch12_power 1.4
modem_192.168.100.1_downstream_ch12_snr 40.37
modem_192.168.100.1_downstream_ch12_uncorrectables 14659.0
modem_192.168.100.1_downstream_ch13_channelid 13.0
modem_192.168.100.1_downstream_ch13_corrected 945.0
modem_192.168.100.1_downstream_ch13_frequency 561.0
modem_192.168.100.1_downstream_ch13_power 1.6
modem_192.168.100.1_downstream_ch13_snr 40.37
modem_192.168.100.1_downstream_ch13_uncorrectables 17343.0
modem_192.168.100.1_downstream_ch14_channelid 14.0
modem_192.168.100.1_downstream_ch14_corrected 606.0
modem_192.168.100.1_downstream_ch14_frequency 567.0
modem_192.168.100.1_downstream_ch14_power 1.7
modem_192.168.100.1_downstream_ch14_snr 40.37
modem_192.168.100.1_downstream_ch14_uncorrectables 17909.0
modem_192.168.100.1_downstream_ch15_channelid 15.0
modem_192.168.100.1_downstream_ch15_corrected 532.0
modem_192.168.100.1_downstream_ch15_frequency 573.0
modem_192.168.100.1_downstream_ch15_power 1.9
modem_192.168.100.1_downstream_ch15_snr 40.95
modem_192.168.100.1_downstream_ch15_uncorrectables 17370.0
modem_192.168.100.1_downstream_ch16_channelid 16.0
modem_192.168.100.1_downstream_ch16_corrected 618.0
modem_192.168.100.1_downstream_ch16_frequency 579.0
modem_192.168.100.1_downstream_ch16_power 2.0
modem_192.168.100.1_downstream_ch16_snr 40.95
modem_192.168.100.1_downstream_ch16_uncorrectables 17292.0
modem_192.168.100.1_downstream_ch17_channelid 18.0
modem_192.168.100.1_downstream_ch17_corrected 287.0
modem_192.168.100.1_downstream_ch17_frequency 591.0
modem_192.168.100.1_downstream_ch17_power 1.7
modem_192.168.100.1_downstream_ch17_snr 40.37
modem_192.168.100.1_downstream_ch17_uncorrectables 7295.0
modem_192.168.100.1_downstream_ch18_channelid 19.0
modem_192.168.100.1_downstream_ch18_corrected 813.0
modem_192.168.100.1_downstream_ch18_frequency 597.0
modem_192.168.100.1_downstream_ch18_power 1.4
modem_192.168.100.1_downstream_ch18_snr 40.37
modem_192.168.100.1_downstream_ch18_uncorrectables 16957.0
modem_192.168.100.1_downstream_ch19_channelid 20.0
modem_192.168.100.1_downstream_ch19_corrected 387.0
modem_192.168.100.1_downstream_ch19_frequency 603.0
modem_192.168.100.1_downstream_ch19_power 1.5
modem_192.168.100.1_downstream_ch19_snr 40.37
modem_192.168.100.1_downstream_ch19_uncorrectables 6319.0
modem_192.168.100.1_downstream_ch20_channelid 21.0
modem_192.168.100.1_downstream_ch20_corrected 499.0
modem_192.168.100.1_downstream_ch20_frequency 609.0
modem_192.168.100.1_downstream_ch20_power 1.7
modem_192.168.100.1_downstream_ch20_snr 40.37
modem_192.168.100.1_downstream_ch20_uncorrectables 18283.0
modem_192.168.100.1_downstream_ch21_channelid 22.0
modem_192.168.100.1_downstream_ch21_corrected 354.0
modem_192.168.100.1_downstream_ch21_frequency 615.0
modem_192.168.100.1_downstream_ch21_power 1.8
modem_192.168.100.1_downstream_ch21_snr 40.37
modem_192.168.100.1_downstream_ch21_uncorrectables 17507.0
modem_192.168.100.1_downstream_ch22_channelid 23.0
modem_192.168.100.1_downstream_ch22_corrected 542.0
modem_192.168.100.1_downstream_ch22_frequency 621.0
modem_192.168.100.1_downstream_ch22_power 1.8
modem_192.168.100.1_downstream_ch22_snr 40.37
modem_192.168.100.1_downstream_ch22_uncorrectables 16858.0
modem_192.168.100.1_downstream_ch23_channelid 24.0
modem_192.168.100.1_downstream_ch23_corrected 224.0
modem_192.168.100.1_downstream_ch23_frequency 627.0
modem_192.168.100.1_downstream_ch23_power 1.9
modem_192.168.100.1_downstream_ch23_snr 40.37
modem_192.168.100.1_downstream_ch23_uncorrectables 20702.0
modem_192.168.100.1_downstream_ch24_channelid 25.0
modem_192.168.100.1_downstream_ch24_corrected 1396.0
modem_192.168.100.1_downstream_ch24_frequency 633.0
modem_192.168.100.1_downstream_ch24_power 2.0
modem_192.168.100.1_downstream_ch24_snr 40.37
modem_192.168.100.1_downstream_ch24_uncorrectables 17471.0
modem_192.168.100.1_downstream_ch25_channelid 26.0
modem_192.168.100.1_downstream_ch25_corrected 448.0
modem_192.168.100.1_downstream_ch25_frequency 639.0
modem_192.168.100.1_downstream_ch25_power 1.9
modem_192.168.100.1_downstream_ch25_snr 39.9
modem_192.168.100.1_downstream_ch25_uncorrectables 20508.0
modem_192.168.100.1_downstream_ch26_channelid 27.0
modem_192.168.100.1_downstream_ch26_corrected 478.0
modem_192.168.100.1_downstream_ch26_frequency 645.0
modem_192.168.100.1_downstream_ch26_power 2.3
modem_192.168.100.1_downstream_ch26_snr 40.4
modem_192.168.100.1_downstream_ch26_uncorrectables 19241.0
modem_192.168.100.1_downstream_ch27_channelid 28.0
modem_192.168.100.1_downstream_ch27_corrected 226.0
modem_192.168.100.1_downstream_ch27_frequency 651.0
modem_192.168.100.1_downstream_ch27_power 1.9
modem_192.168.100.1_downstream_ch27_snr 39.9
modem_192.168.100.1_downstream_ch27_uncorrectables 20313.0
modem_192.168.100.1_downstream_ch28_channelid 29.0
modem_192.168.100.1_downstream_ch28_corrected 506.0
modem_192.168.100.1_downstream_ch28_frequency 657.0
modem_192.168.100.1_downstream_ch28_power 1.6
modem_192.168.100.1_downstream_ch28_snr 40.4
modem_192.168.100.1_downstream_ch28_uncorrectables 19369.0
modem_192.168.100.1_downstream_ch29_channelid 30.0
modem_192.168.100.1_downstream_ch29_corrected 969.0
modem_192.168.100.1_downstream_ch29_frequency 663.0
modem_192.168.100.1_downstream_ch29_power 1.8
modem_192.168.100.1_downstream_ch29_snr 41.1
modem_192.168.100.1_downstream_ch29_uncorrectables 9814.0
modem_192.168.100.1_downstream_ch30_channelid 31.0
modem_192.168.100.1_downstream_ch30_corrected 1011.0
modem_192.168.100.1_downstream_ch30_frequency 669.0
modem_192.168.100.1_downstream_ch30_power 1.9
modem_192.168.100.1_downstream_ch30_snr 41.1
modem_192.168.100.1_downstream_ch30_uncorrectables 20027.0
modem_192.168.100.1_downstream_ch31_channelid 32.0
modem_192.168.100.1_downstream_ch31_corrected 104.0
modem_192.168.100.1_downstream_ch31_frequency 675.0
modem_192.168.100.1_downstream_ch31_power 2.1
modem_192.168.100.1_downstream_ch31_snr 40.4
modem_192.168.100.1_downstream_ch31_uncorrectables 2891.0
modem_192.168.100.1_downstream_channel_count 31
modem_192.168.100.1_upstream_ch1_channelid 66.0
modem_192.168.100.1_upstream_ch1_frequency 24.0
modem_192.168.100.1_upstream_ch1_power 45.25
modem_192.168.100.1_upstream_ch1_symbolrate 5120.0
modem_192.168.100.1_upstream_ch2_channelid 68.0
modem_192.168.100.1_upstream_ch2_frequency 36.8
modem_192.168.100.1_upstream_ch2_power 44.5
modem_192.168.100.1_upstream_ch2_symbolrate 5120.0
modem_192.168.100.1_upstream_ch3_channelid 67.0
modem_192.168.100.1_upstream_ch3_frequency 30.4
modem_192.168.100.1_upstream_ch3_power 45.0
modem_192.168.100.1_upstream_ch3_symbolrate 5120.0
modem_192.168.100.1_upstream_ch4_channelid 65.0
modem_192.168.100.1_upstream_ch4_frequency 19.2
modem_192.168.100.1_upstream_ch4_power 44.75
modem_192.168.100.1_upstream_ch4_symbolrate 2560.0
modem_192.168.100.1_upstream_channel_count 4
```
