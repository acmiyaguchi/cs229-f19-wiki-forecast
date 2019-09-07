# `data` folder structure

```bash
data
├── [ 224]  bzipped
│   ├── [ 18M]  enwiki-20190820-category.sql.bz2
│   ├── [1.8G]  enwiki-20190820-categorylinks.sql.bz2
│   ├── [1.3G]  enwiki-20190820-page.sql.bz2
│   ├── [5.0G]  enwiki-20190820-pagelinks.sql.bz2
│   └── [101M]  enwiki-20190820-redirect.sql.bz2
├── [ 192]  enwiki
│   ├── [ 256]  categorylinks
│   │   ├── [   0]  _SUCCESS
│   │   ├── [222M]  part-00000-5c4ff747-a7d2-48b6-8e21-e82a4b8840dd-c000.snappy.parquet
│   │   └── [233M]  part-00001-5c4ff747-a7d2-48b6-8e21-e82a4b8840dd-c000.snappy.parquet
│   ├── [ 192]  categorypages
│   │   ├── [   0]  _SUCCESS
│   │   └── [ 32M]  part-00000-e856fb1e-f22c-4c36-9ed1-5621bab499a9-c000.snappy.parquet
│   ├── [ 640]  pagelinks
│   │   ├── [   0]  _SUCCESS
│   │   ├── [248M]  part-00000-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   │   ├── [231M]  part-00001-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   │   ├── [245M]  part-00002-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   │   ├── [247M]  part-00003-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   │   ├── [248M]  part-00004-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   │   ├── [247M]  part-00005-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   │   ├── [251M]  part-00006-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   │   └── [240M]  part-00007-3255198c-5b01-46f9-9a29-0e7e6c3d24c1-c000.snappy.parquet
│   └── [ 192]  pages
│       ├── [   0]  _SUCCESS
│       └── [117M]  part-00000-210e029a-635e-4a0e-9f69-7e7d135072bd-c000.snappy.parquet
├── [ 160]  processed
│   ├── [ 13K]  categorylinks
│   │   ├── [   0]  _SUCCESS
│   │   ├── [2.2M]  part-00000-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00001-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00002-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00003-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00004-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00005-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [4.3M]  part-00006-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00007-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.3M]  part-00008-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00009-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00010-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00011-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00012-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00013-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00014-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.0M]  part-00015-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00016-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00017-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00018-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.2M]  part-00019-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00020-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.2M]  part-00021-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00022-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00023-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.2M]  part-00024-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00025-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00026-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00027-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00028-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00029-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00030-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00031-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.5M]  part-00032-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00033-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00034-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.4M]  part-00035-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00036-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00037-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [6.4M]  part-00038-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.8M]  part-00039-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00040-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.1M]  part-00041-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.4M]  part-00042-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00043-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00044-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00045-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00046-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00047-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00048-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00049-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00050-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00051-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00052-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00053-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00054-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00055-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00056-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00057-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.0M]  part-00058-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00059-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00060-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.1M]  part-00061-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00062-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00063-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00064-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00065-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00066-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [4.3M]  part-00067-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00068-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00069-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00070-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00071-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00072-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [7.0M]  part-00073-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.3M]  part-00074-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.5M]  part-00075-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00076-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00077-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00078-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00079-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [6.8M]  part-00080-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.1M]  part-00081-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.0M]  part-00082-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00083-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00084-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.4M]  part-00085-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00086-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.7M]  part-00087-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00088-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00089-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00090-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00091-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00092-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00093-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00094-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.0M]  part-00095-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00096-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00097-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.5M]  part-00098-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [8.6M]  part-00099-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00100-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.4M]  part-00101-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00102-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00103-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00104-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00105-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00106-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.1M]  part-00107-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00108-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00109-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00110-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00111-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.2M]  part-00112-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00113-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.2M]  part-00114-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00115-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00116-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00117-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00118-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.1M]  part-00119-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00120-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00121-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.0M]  part-00122-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00123-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00124-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00125-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00126-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00127-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.4M]  part-00128-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00129-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00130-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00131-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.1M]  part-00132-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00133-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00134-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00135-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00136-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00137-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00138-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00139-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00140-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.0M]  part-00141-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00142-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [ 11M]  part-00143-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00144-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00145-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00146-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00147-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.1M]  part-00148-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00149-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00150-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.2M]  part-00151-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00152-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00153-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.1M]  part-00154-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.1M]  part-00155-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [6.5M]  part-00156-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00157-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00158-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00159-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00160-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00161-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00162-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00163-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00164-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00165-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.3M]  part-00166-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00167-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00168-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00169-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00170-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.2M]  part-00171-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00172-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00173-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00174-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.8M]  part-00175-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.0M]  part-00176-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00177-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00178-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.7M]  part-00179-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.2M]  part-00180-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.5M]  part-00181-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.0M]  part-00182-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [5.0M]  part-00183-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.9M]  part-00184-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.0M]  part-00185-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.2M]  part-00186-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [2.2M]  part-00187-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00188-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [4.4M]  part-00189-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.3M]  part-00190-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00191-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [3.2M]  part-00192-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00193-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00194-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00195-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.6M]  part-00196-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.4M]  part-00197-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   ├── [1.5M]  part-00198-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   │   └── [1.7M]  part-00199-3c91fb13-be76-49d9-8a1c-fa168cc8f1dd-c000.csv.gz
│   ├── [ 128]  page
│   │   ├── [2.6K]  category_pages
│   │   │   ├── [   0]  _SUCCESS
│   │   │   ├── [325K]  part-00000-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [342K]  part-00001-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [353K]  part-00002-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [314K]  part-00003-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [337K]  part-00004-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [335K]  part-00005-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [378K]  part-00006-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [334K]  part-00007-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [320K]  part-00008-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [395K]  part-00009-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [379K]  part-00010-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [339K]  part-00011-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [355K]  part-00012-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [451K]  part-00013-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [441K]  part-00014-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [469K]  part-00015-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [528K]  part-00016-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [461K]  part-00017-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [607K]  part-00018-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [725K]  part-00019-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [641K]  part-00020-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [587K]  part-00021-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [722K]  part-00022-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [848K]  part-00023-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [678K]  part-00024-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [579K]  part-00025-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [607K]  part-00026-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [645K]  part-00027-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [523K]  part-00028-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [711K]  part-00029-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [637K]  part-00030-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [665K]  part-00031-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [789K]  part-00032-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [1.0M]  part-00033-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [645K]  part-00034-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [629K]  part-00035-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [605K]  part-00036-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [583K]  part-00037-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   ├── [657K]  part-00038-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   │   └── [593K]  part-00039-6b29d909-7dcc-43d6-b80b-aa758e366fda-c000.csv.gz
│   │   └── [2.6K]  normal_pages
│   │       ├── [   0]  _SUCCESS
│   │       ├── [5.6M]  part-00000-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [4.3M]  part-00001-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [3.3M]  part-00002-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.8M]  part-00003-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.4M]  part-00004-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.1M]  part-00005-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.6M]  part-00006-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.1M]  part-00007-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00008-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00009-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.1M]  part-00010-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.9M]  part-00011-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.0M]  part-00012-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [2.1M]  part-00013-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.9M]  part-00014-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00015-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.7M]  part-00016-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.5M]  part-00017-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.9M]  part-00018-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00019-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.7M]  part-00020-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00021-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.7M]  part-00022-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.7M]  part-00023-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00024-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00025-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.8M]  part-00026-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.6M]  part-00027-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.3M]  part-00028-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.5M]  part-00029-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.5M]  part-00030-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.3M]  part-00031-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.5M]  part-00032-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.5M]  part-00033-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.4M]  part-00034-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.4M]  part-00035-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.6M]  part-00036-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.3M]  part-00037-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       ├── [1.2M]  part-00038-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   │       └── [1.3M]  part-00039-4dc2ee3e-a72a-4725-8bdb-e66b69e24276-c000.csv.gz
│   └── [ 13K]  pagelinks
│       ├── [   0]  _SUCCESS
│       ├── [ 11M]  part-00000-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00001-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00002-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00003-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00004-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00005-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00006-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00007-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00008-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00009-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00010-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00011-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00012-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00013-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00014-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00015-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00016-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00017-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00018-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00019-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00020-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00021-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00022-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00023-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00024-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00025-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00026-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00027-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00028-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00029-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00030-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00031-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00032-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00033-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00034-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00035-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00036-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00037-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00038-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00039-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00040-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00041-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00042-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00043-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00044-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00045-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00046-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00047-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00048-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00049-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00050-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00051-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00052-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00053-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00054-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00055-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00056-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00057-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00058-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00059-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00060-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00061-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00062-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00063-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00064-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00065-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00066-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00067-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00068-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00069-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00070-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00071-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00072-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00073-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00074-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00075-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00076-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00077-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00078-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00079-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00080-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00081-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00082-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00083-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00084-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00085-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00086-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00087-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00088-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00089-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00090-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00091-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00092-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00093-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00094-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00095-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00096-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00097-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00098-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00099-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00100-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00101-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00102-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00103-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00104-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00105-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00106-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00107-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00108-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00109-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00110-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00111-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00112-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00113-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00114-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00115-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00116-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00117-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00118-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00119-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00120-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00121-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00122-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00123-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00124-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00125-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00126-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00127-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00128-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00129-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00130-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00131-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00132-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00133-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00134-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00135-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00136-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00137-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00138-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00139-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00140-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00141-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00142-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00143-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00144-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00145-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00146-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00147-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00148-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00149-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00150-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00151-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00152-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00153-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00154-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00155-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00156-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00157-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00158-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00159-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00160-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00161-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00162-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00163-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00164-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00165-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00166-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00167-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00168-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00169-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00170-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00171-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00172-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00173-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00174-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00175-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00176-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00177-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00178-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00179-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00180-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00181-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00182-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00183-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00184-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00185-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00186-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00187-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00188-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00189-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00190-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00191-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00192-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00193-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00194-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00195-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00196-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00197-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       ├── [ 11M]  part-00198-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
│       └── [ 11M]  part-00199-d51952cc-1f4a-46a1-aba5-023a3f5777d3-c000.csv.gz
└── [ 224]  raw
    ├── [ 24M]  enwiki-20190820-category.sql.gz
    ├── [2.5G]  enwiki-20190820-categorylinks.sql.gz
    ├── [1.6G]  enwiki-20190820-page.sql.gz
    ├── [6.0G]  enwiki-20190820-pagelinks.sql.gz
    └── [126M]  enwiki-20190820-redirect.sql.gz

13 directories, 510 files
```
