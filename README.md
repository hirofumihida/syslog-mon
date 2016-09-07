# syslog-mon

## execute sample

```
% python syslog-mon.py
parsed: {'timestamp': 'Sep 7 18:26:55', 'message': '[24043718.285047] md/raid:md127: Disk failure on sdg1, disabling device.', 'hostname': 'fs2', 'appname': 'kernel'}
```

```
% tail -3 syslog
Sep  7 18:22:55 fs2 kernel: [24043718.285044] md/raid:md127: Too many read errors, failing device sdg1.
Sep  7 18:26:55 fs2 kernel: [24043718.285047] md/raid:md127: Disk failure on sdg1, disabling device.
Sep  7 18:26:55 fs2 kernel: [24043718.285047] md/raid:md127: Operation continuing on 9 devices.
```