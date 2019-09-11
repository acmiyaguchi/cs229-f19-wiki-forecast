# `data` folder structure

```bash
data
├── [ 224]  bzipped
│   ├── [ 18M]  enwiki-20190820-category.sql.bz2
│   ├── [1.8G]  enwiki-20190820-categorylinks.sql.bz2
│   ├── [1.3G]  enwiki-20190820-page.sql.bz2
│   ├── [5.0G]  enwiki-20190820-pagelinks.sql.bz2
│   └── [101M]  enwiki-20190820-redirect.sql.bz2
├── [ 256]  enwiki
│   ├── [ 256]  categorylinks
│   │   ├── [   0]  _SUCCESS
│   │   ├── [222M]  part-00000-5c4ff747-a7d2-48b6-8e21-e82a4b8840dd-c000.snappy.parquet
│   │   └── [233M]  part-00001-5c4ff747-a7d2-48b6-8e21-e82a4b8840dd-c000.snappy.parquet
│   ├── [ 192]  categorypages
│   │   ├── [   0]  _SUCCESS
│   │   └── [ 32M]  part-00000-e856fb1e-f22c-4c36-9ed1-5621bab499a9-c000.snappy.parquet
│   ├── [ 384]  page_parquet
│   │   ├── [   0]  _SUCCESS
│   │   ├── [179M]  part-00000-e97ee0ca-9896-4efe-88a7-8cf2080e6443-c000.snappy.parquet
│   │   ├── [175M]  part-00001-e97ee0ca-9896-4efe-88a7-8cf2080e6443-c000.snappy.parquet
│   │   ├── [181M]  part-00002-e97ee0ca-9896-4efe-88a7-8cf2080e6443-c000.snappy.parquet
│   │   └── [182M]  part-00003-e97ee0ca-9896-4efe-88a7-8cf2080e6443-c000.snappy.parquet
│   ├── [ 192]  pagecount_daily_v1
│   │   ├── [   0]  _SUCCESS
│   │   └── [ 63M]  part-00000-403e555c-eed5-4476-8908-b019dfcd08d4-c000.snappy.parquet
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
├── [ 224]  processed
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
│   ├── [2.6K]  page_parquet
│   │   ├── [   0]  _SUCCESS
│   │   ├── [ 27M]  part-00000-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 23M]  part-00001-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 18M]  part-00002-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 15M]  part-00003-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 14M]  part-00004-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00005-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 15M]  part-00006-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 14M]  part-00007-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 14M]  part-00008-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00009-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 13M]  part-00010-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00011-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00012-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 14M]  part-00013-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00014-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00015-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 13M]  part-00016-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00017-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00018-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00019-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00020-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00021-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 13M]  part-00022-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 13M]  part-00023-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00024-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00025-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00026-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00027-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [8.8M]  part-00028-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00029-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00030-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 12M]  part-00031-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00032-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00033-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00034-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00035-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 11M]  part-00036-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [9.9M]  part-00037-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   ├── [ 10M]  part-00038-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   │   └── [ 11M]  part-00039-dafb471a-f403-44e1-8b43-5ee7478e8c63-c000.gz.parquet
│   ├── [ 13K]  pagecount
│   │   ├── [   0]  _SUCCESS
│   │   ├── [ 23M]  part-00000-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00001-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00002-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00003-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00004-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00005-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00006-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00007-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00008-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00009-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00010-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00011-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00012-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00013-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00014-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00015-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00016-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00017-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00018-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00019-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00020-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00021-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00022-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00023-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00024-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00025-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00026-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00027-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00028-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00029-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00030-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00031-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00032-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00033-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00034-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00035-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00036-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00037-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00038-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00039-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00040-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00041-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00042-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00043-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00044-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00045-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00046-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00047-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00048-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00049-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00050-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00051-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00052-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00053-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00054-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00055-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00056-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00057-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00058-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00059-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00060-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00061-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00062-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00063-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00064-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00065-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00066-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00067-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00068-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 25M]  part-00069-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00070-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00071-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00072-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00073-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00074-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00075-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00076-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00077-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00078-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00079-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00080-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00081-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00082-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00083-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00084-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00085-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00086-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00087-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00088-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00089-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00090-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00091-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00092-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00093-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00094-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00095-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00096-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00097-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00098-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00099-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00100-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00101-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00102-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00103-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00104-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00105-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00106-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00107-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 25M]  part-00108-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00109-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00110-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00111-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00112-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00113-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00114-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00115-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00116-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00117-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00118-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00119-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00120-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00121-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00122-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00123-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 25M]  part-00124-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00125-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00126-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00127-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00128-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00129-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00130-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00131-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00132-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00133-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00134-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00135-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00136-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00137-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00138-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00139-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00140-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00141-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00142-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00143-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00144-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00145-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00146-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00147-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00148-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00149-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00150-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00151-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00152-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00153-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00154-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00155-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00156-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00157-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00158-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00159-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00160-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00161-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00162-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00163-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00164-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00165-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00166-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00167-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00168-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00169-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00170-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00171-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00172-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00173-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00174-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00175-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00176-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00177-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00178-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00179-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00180-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00181-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00182-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00183-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00184-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00185-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00186-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00187-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00188-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00189-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00190-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00191-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 22M]  part-00192-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 21M]  part-00193-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00194-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00195-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00196-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 23M]  part-00197-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   ├── [ 24M]  part-00198-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
│   │   └── [ 22M]  part-00199-78235a89-2349-46ca-bba8-eee118d88359-c000.gz.parquet
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
└── [ 256]  raw
    ├── [ 24M]  enwiki-20190820-category.sql.gz
    ├── [2.5G]  enwiki-20190820-categorylinks.sql.gz
    ├── [1.6G]  enwiki-20190820-page.sql.gz
    ├── [6.0G]  enwiki-20190820-pagelinks.sql.gz
    ├── [126M]  enwiki-20190820-redirect.sql.gz
    └── [ 19K]  pagecounts
        ├── [4.2K]  index.html.tmp
        ├── [343M]  pagecounts-2018-01-01.bz2
        ├── [378M]  pagecounts-2018-01-02.bz2
        ├── [387M]  pagecounts-2018-01-03.bz2
        ├── [378M]  pagecounts-2018-01-04.bz2
        ├── [373M]  pagecounts-2018-01-05.bz2
        ├── [386M]  pagecounts-2018-01-06.bz2
        ├── [383M]  pagecounts-2018-01-07.bz2
        ├── [389M]  pagecounts-2018-01-08.bz2
        ├── [387M]  pagecounts-2018-01-09.bz2
        ├── [384M]  pagecounts-2018-01-10.bz2
        ├── [387M]  pagecounts-2018-01-11.bz2
        ├── [384M]  pagecounts-2018-01-12.bz2
        ├── [375M]  pagecounts-2018-01-13.bz2
        ├── [392M]  pagecounts-2018-01-14.bz2
        ├── [404M]  pagecounts-2018-01-15.bz2
        ├── [389M]  pagecounts-2018-01-16.bz2
        ├── [394M]  pagecounts-2018-01-17.bz2
        ├── [389M]  pagecounts-2018-01-18.bz2
        ├── [368M]  pagecounts-2018-01-19.bz2
        ├── [359M]  pagecounts-2018-01-20.bz2
        ├── [369M]  pagecounts-2018-01-21.bz2
        ├── [380M]  pagecounts-2018-01-22.bz2
        ├── [378M]  pagecounts-2018-01-23.bz2
        ├── [375M]  pagecounts-2018-01-24.bz2
        ├── [374M]  pagecounts-2018-01-25.bz2
        ├── [370M]  pagecounts-2018-01-26.bz2
        ├── [358M]  pagecounts-2018-01-27.bz2
        ├── [376M]  pagecounts-2018-01-28.bz2
        ├── [384M]  pagecounts-2018-01-29.bz2
        ├── [378M]  pagecounts-2018-01-30.bz2
        ├── [381M]  pagecounts-2018-01-31.bz2
        ├── [384M]  pagecounts-2018-02-01.bz2
        ├── [373M]  pagecounts-2018-02-02.bz2
        ├── [366M]  pagecounts-2018-02-03.bz2
        ├── [377M]  pagecounts-2018-02-04.bz2
        ├── [381M]  pagecounts-2018-02-05.bz2
        ├── [383M]  pagecounts-2018-02-06.bz2
        ├── [381M]  pagecounts-2018-02-07.bz2
        ├── [378M]  pagecounts-2018-02-08.bz2
        ├── [364M]  pagecounts-2018-02-09.bz2
        ├── [359M]  pagecounts-2018-02-10.bz2
        ├── [368M]  pagecounts-2018-02-11.bz2
        ├── [381M]  pagecounts-2018-02-12.bz2
        ├── [377M]  pagecounts-2018-02-13.bz2
        ├── [369M]  pagecounts-2018-02-14.bz2
        ├── [374M]  pagecounts-2018-02-15.bz2
        ├── [370M]  pagecounts-2018-02-16.bz2
        ├── [360M]  pagecounts-2018-02-17.bz2
        ├── [376M]  pagecounts-2018-02-18.bz2
        ├── [388M]  pagecounts-2018-02-19.bz2
        ├── [389M]  pagecounts-2018-02-20.bz2
        ├── [385M]  pagecounts-2018-02-21.bz2
        ├── [383M]  pagecounts-2018-02-22.bz2
        ├── [375M]  pagecounts-2018-02-23.bz2
        ├── [366M]  pagecounts-2018-02-24.bz2
        ├── [383M]  pagecounts-2018-02-25.bz2
        ├── [396M]  pagecounts-2018-02-26.bz2
        ├── [388M]  pagecounts-2018-02-27.bz2
        ├── [381M]  pagecounts-2018-02-28.bz2
        ├── [375M]  pagecounts-2018-03-01.bz2
        ├── [370M]  pagecounts-2018-03-02.bz2
        ├── [356M]  pagecounts-2018-03-03.bz2
        ├── [369M]  pagecounts-2018-03-04.bz2
        ├── [377M]  pagecounts-2018-03-05.bz2
        ├── [378M]  pagecounts-2018-03-06.bz2
        ├── [379M]  pagecounts-2018-03-07.bz2
        ├── [374M]  pagecounts-2018-03-08.bz2
        ├── [370M]  pagecounts-2018-03-09.bz2
        ├── [357M]  pagecounts-2018-03-10.bz2
        ├── [374M]  pagecounts-2018-03-11.bz2
        ├── [381M]  pagecounts-2018-03-12.bz2
        ├── [378M]  pagecounts-2018-03-13.bz2
        ├── [377M]  pagecounts-2018-03-14.bz2
        ├── [380M]  pagecounts-2018-03-15.bz2
        ├── [368M]  pagecounts-2018-03-16.bz2
        ├── [362M]  pagecounts-2018-03-17.bz2
        ├── [375M]  pagecounts-2018-03-18.bz2
        ├── [381M]  pagecounts-2018-03-19.bz2
        ├── [388M]  pagecounts-2018-03-20.bz2
        ├── [391M]  pagecounts-2018-03-21.bz2
        ├── [387M]  pagecounts-2018-03-22.bz2
        ├── [376M]  pagecounts-2018-03-23.bz2
        ├── [357M]  pagecounts-2018-03-24.bz2
        ├── [373M]  pagecounts-2018-03-25.bz2
        ├── [379M]  pagecounts-2018-03-26.bz2
        ├── [376M]  pagecounts-2018-03-27.bz2
        ├── [370M]  pagecounts-2018-03-28.bz2
        ├── [365M]  pagecounts-2018-03-29.bz2
        ├── [365M]  pagecounts-2018-03-30.bz2
        ├── [358M]  pagecounts-2018-03-31.bz2
        ├── [366M]  pagecounts-2018-04-01.bz2
        ├── [382M]  pagecounts-2018-04-02.bz2
        ├── [379M]  pagecounts-2018-04-03.bz2
        ├── [375M]  pagecounts-2018-04-04.bz2
        ├── [375M]  pagecounts-2018-04-05.bz2
        ├── [364M]  pagecounts-2018-04-06.bz2
        ├── [352M]  pagecounts-2018-04-07.bz2
        ├── [366M]  pagecounts-2018-04-08.bz2
        ├── [381M]  pagecounts-2018-04-09.bz2
        ├── [378M]  pagecounts-2018-04-10.bz2
        ├── [380M]  pagecounts-2018-04-11.bz2
        ├── [376M]  pagecounts-2018-04-12.bz2
        ├── [365M]  pagecounts-2018-04-13.bz2
        ├── [352M]  pagecounts-2018-04-14.bz2
        ├── [380M]  pagecounts-2018-04-15.bz2
        ├── [388M]  pagecounts-2018-04-16.bz2
        ├── [388M]  pagecounts-2018-04-17.bz2
        ├── [383M]  pagecounts-2018-04-18.bz2
        ├── [376M]  pagecounts-2018-04-19.bz2
        ├── [369M]  pagecounts-2018-04-20.bz2
        ├── [355M]  pagecounts-2018-04-21.bz2
        ├── [374M]  pagecounts-2018-04-22.bz2
        ├── [386M]  pagecounts-2018-04-23.bz2
        ├── [380M]  pagecounts-2018-04-24.bz2
        ├── [383M]  pagecounts-2018-04-25.bz2
        ├── [378M]  pagecounts-2018-04-26.bz2
        ├── [362M]  pagecounts-2018-04-27.bz2
        ├── [343M]  pagecounts-2018-04-28.bz2
        ├── [355M]  pagecounts-2018-04-29.bz2
        ├── [366M]  pagecounts-2018-04-30.bz2
        ├── [371M]  pagecounts-2018-05-01.bz2
        ├── [375M]  pagecounts-2018-05-02.bz2
        ├── [375M]  pagecounts-2018-05-03.bz2
        ├── [366M]  pagecounts-2018-05-04.bz2
        ├── [353M]  pagecounts-2018-05-05.bz2
        ├── [366M]  pagecounts-2018-05-06.bz2
        ├── [384M]  pagecounts-2018-05-07.bz2
        ├── [379M]  pagecounts-2018-05-08.bz2
        ├── [370M]  pagecounts-2018-05-09.bz2
        ├── [374M]  pagecounts-2018-05-10.bz2
        ├── [365M]  pagecounts-2018-05-11.bz2
        ├── [352M]  pagecounts-2018-05-12.bz2
        ├── [367M]  pagecounts-2018-05-13.bz2
        ├── [385M]  pagecounts-2018-05-14.bz2
        ├── [386M]  pagecounts-2018-05-15.bz2
        ├── [385M]  pagecounts-2018-05-16.bz2
        ├── [383M]  pagecounts-2018-05-17.bz2
        ├── [366M]  pagecounts-2018-05-18.bz2
        ├── [348M]  pagecounts-2018-05-19.bz2
        ├── [365M]  pagecounts-2018-05-20.bz2
        ├── [381M]  pagecounts-2018-05-21.bz2
        ├── [379M]  pagecounts-2018-05-22.bz2
        ├── [383M]  pagecounts-2018-05-23.bz2
        ├── [375M]  pagecounts-2018-05-24.bz2
        ├── [363M]  pagecounts-2018-05-25.bz2
        ├── [347M]  pagecounts-2018-05-26.bz2
        ├── [366M]  pagecounts-2018-05-27.bz2
        ├── [377M]  pagecounts-2018-05-28.bz2
        ├── [379M]  pagecounts-2018-05-29.bz2
        ├── [377M]  pagecounts-2018-05-30.bz2
        ├── [371M]  pagecounts-2018-05-31.bz2
        ├── [366M]  pagecounts-2018-06-01.bz2
        ├── [356M]  pagecounts-2018-06-02.bz2
        ├── [376M]  pagecounts-2018-06-03.bz2
        ├── [383M]  pagecounts-2018-06-04.bz2
        ├── [379M]  pagecounts-2018-06-05.bz2
        ├── [383M]  pagecounts-2018-06-06.bz2
        ├── [380M]  pagecounts-2018-06-07.bz2
        ├── [369M]  pagecounts-2018-06-08.bz2
        ├── [357M]  pagecounts-2018-06-09.bz2
        ├── [369M]  pagecounts-2018-06-10.bz2
        ├── [379M]  pagecounts-2018-06-11.bz2
        ├── [373M]  pagecounts-2018-06-12.bz2
        ├── [377M]  pagecounts-2018-06-13.bz2
        ├── [361M]  pagecounts-2018-06-14.bz2
        ├── [362M]  pagecounts-2018-06-15.bz2
        ├── [344M]  pagecounts-2018-06-16.bz2
        ├── [359M]  pagecounts-2018-06-17.bz2
        ├── [368M]  pagecounts-2018-06-18.bz2
        ├── [369M]  pagecounts-2018-06-19.bz2
        ├── [365M]  pagecounts-2018-06-20.bz2
        ├── [362M]  pagecounts-2018-06-21.bz2
        ├── [359M]  pagecounts-2018-06-22.bz2
        ├── [353M]  pagecounts-2018-06-23.bz2
        ├── [364M]  pagecounts-2018-06-24.bz2
        ├── [370M]  pagecounts-2018-06-25.bz2
        ├── [366M]  pagecounts-2018-06-26.bz2
        ├── [359M]  pagecounts-2018-06-27.bz2
        ├── [363M]  pagecounts-2018-06-28.bz2
        ├── [358M]  pagecounts-2018-06-29.bz2
        ├── [356M]  pagecounts-2018-06-30.bz2
        ├── [360M]  pagecounts-2018-07-01.bz2
        ├── [371M]  pagecounts-2018-07-02.bz2
        ├── [366M]  pagecounts-2018-07-03.bz2
        ├── [361M]  pagecounts-2018-07-04.bz2
        ├── [366M]  pagecounts-2018-07-05.bz2
        ├── [357M]  pagecounts-2018-07-06.bz2
        ├── [350M]  pagecounts-2018-07-07.bz2
        ├── [363M]  pagecounts-2018-07-08.bz2
        ├── [376M]  pagecounts-2018-07-09.bz2
        ├── [378M]  pagecounts-2018-07-10.bz2
        ├── [392M]  pagecounts-2018-07-11.bz2
        ├── [387M]  pagecounts-2018-07-12.bz2
        ├── [367M]  pagecounts-2018-07-13.bz2
        ├── [348M]  pagecounts-2018-07-14.bz2
        ├── [360M]  pagecounts-2018-07-15.bz2
        ├── [369M]  pagecounts-2018-07-16.bz2
        ├── [372M]  pagecounts-2018-07-17.bz2
        ├── [367M]  pagecounts-2018-07-18.bz2
        ├── [365M]  pagecounts-2018-07-19.bz2
        ├── [357M]  pagecounts-2018-07-20.bz2
        ├── [344M]  pagecounts-2018-07-21.bz2
        ├── [361M]  pagecounts-2018-07-22.bz2
        ├── [371M]  pagecounts-2018-07-23.bz2
        ├── [369M]  pagecounts-2018-07-24.bz2
        ├── [368M]  pagecounts-2018-07-25.bz2
        ├── [364M]  pagecounts-2018-07-26.bz2
        ├── [356M]  pagecounts-2018-07-27.bz2
        ├── [351M]  pagecounts-2018-07-28.bz2
        ├── [361M]  pagecounts-2018-07-29.bz2
        ├── [375M]  pagecounts-2018-07-30.bz2
        ├── [373M]  pagecounts-2018-07-31.bz2
        ├── [370M]  pagecounts-2018-08-01.bz2
        ├── [370M]  pagecounts-2018-08-02.bz2
        ├── [365M]  pagecounts-2018-08-03.bz2
        ├── [354M]  pagecounts-2018-08-04.bz2
        ├── [359M]  pagecounts-2018-08-05.bz2
        ├── [372M]  pagecounts-2018-08-06.bz2
        ├── [372M]  pagecounts-2018-08-07.bz2
        ├── [364M]  pagecounts-2018-08-08.bz2
        ├── [363M]  pagecounts-2018-08-09.bz2
        ├── [357M]  pagecounts-2018-08-10.bz2
        ├── [341M]  pagecounts-2018-08-11.bz2
        ├── [354M]  pagecounts-2018-08-12.bz2
        ├── [372M]  pagecounts-2018-08-13.bz2
        ├── [368M]  pagecounts-2018-08-14.bz2
        ├── [375M]  pagecounts-2018-08-15.bz2
        ├── [378M]  pagecounts-2018-08-16.bz2
        ├── [373M]  pagecounts-2018-08-17.bz2
        ├── [355M]  pagecounts-2018-08-18.bz2
        ├── [374M]  pagecounts-2018-08-19.bz2
        ├── [391M]  pagecounts-2018-08-20.bz2
        ├── [386M]  pagecounts-2018-08-21.bz2
        ├── [393M]  pagecounts-2018-08-22.bz2
        ├── [384M]  pagecounts-2018-08-23.bz2
        ├── [384M]  pagecounts-2018-08-24.bz2
        ├── [364M]  pagecounts-2018-08-25.bz2
        ├── [375M]  pagecounts-2018-08-26.bz2
        ├── [392M]  pagecounts-2018-08-27.bz2
        ├── [390M]  pagecounts-2018-08-28.bz2
        ├── [395M]  pagecounts-2018-08-29.bz2
        ├── [383M]  pagecounts-2018-08-30.bz2
        ├── [377M]  pagecounts-2018-08-31.bz2
        ├── [354M]  pagecounts-2018-09-01.bz2
        ├── [365M]  pagecounts-2018-09-02.bz2
        ├── [384M]  pagecounts-2018-09-03.bz2
        ├── [398M]  pagecounts-2018-09-04.bz2
        ├── [393M]  pagecounts-2018-09-05.bz2
        ├── [391M]  pagecounts-2018-09-06.bz2
        ├── [392M]  pagecounts-2018-09-07.bz2
        ├── [362M]  pagecounts-2018-09-08.bz2
        ├── [365M]  pagecounts-2018-09-09.bz2
        ├── [391M]  pagecounts-2018-09-10.bz2
        ├── [393M]  pagecounts-2018-09-11.bz2
        ├── [389M]  pagecounts-2018-09-12.bz2
        ├── [391M]  pagecounts-2018-09-13.bz2
        ├── [371M]  pagecounts-2018-09-14.bz2
        ├── [376M]  pagecounts-2018-09-15.bz2
        ├── [387M]  pagecounts-2018-09-16.bz2
        ├── [405M]  pagecounts-2018-09-17.bz2
        ├── [392M]  pagecounts-2018-09-18.bz2
        ├── [394M]  pagecounts-2018-09-19.bz2
        ├── [404M]  pagecounts-2018-09-20.bz2
        ├── [391M]  pagecounts-2018-09-21.bz2
        ├── [363M]  pagecounts-2018-09-22.bz2
        ├── [372M]  pagecounts-2018-09-23.bz2
        ├── [389M]  pagecounts-2018-09-24.bz2
        ├── [383M]  pagecounts-2018-09-25.bz2
        ├── [390M]  pagecounts-2018-09-26.bz2
        ├── [378M]  pagecounts-2018-09-27.bz2
        ├── [366M]  pagecounts-2018-09-28.bz2
        ├── [355M]  pagecounts-2018-09-29.bz2
        ├── [375M]  pagecounts-2018-09-30.bz2
        ├── [384M]  pagecounts-2018-10-01.bz2
        ├── [393M]  pagecounts-2018-10-02.bz2
        ├── [401M]  pagecounts-2018-10-03.bz2
        ├── [391M]  pagecounts-2018-10-04.bz2
        ├── [385M]  pagecounts-2018-10-05.bz2
        ├── [370M]  pagecounts-2018-10-06.bz2
        ├── [385M]  pagecounts-2018-10-07.bz2
        ├── [398M]  pagecounts-2018-10-08.bz2
        ├── [399M]  pagecounts-2018-10-09.bz2
        ├── [387M]  pagecounts-2018-10-10.bz2
        ├── [382M]  pagecounts-2018-10-11.bz2
        ├── [372M]  pagecounts-2018-10-12.bz2
        ├── [360M]  pagecounts-2018-10-13.bz2
        ├── [374M]  pagecounts-2018-10-14.bz2
        ├── [397M]  pagecounts-2018-10-15.bz2
        ├── [390M]  pagecounts-2018-10-16.bz2
        ├── [383M]  pagecounts-2018-10-17.bz2
        ├── [388M]  pagecounts-2018-10-18.bz2
        ├── [372M]  pagecounts-2018-10-19.bz2
        ├── [358M]  pagecounts-2018-10-20.bz2
        ├── [384M]  pagecounts-2018-10-21.bz2
        ├── [412M]  pagecounts-2018-10-22.bz2
        ├── [398M]  pagecounts-2018-10-23.bz2
        ├── [423M]  pagecounts-2018-10-24.bz2
        ├── [388M]  pagecounts-2018-10-25.bz2
        ├── [368M]  pagecounts-2018-10-26.bz2
        ├── [358M]  pagecounts-2018-10-27.bz2
        ├── [379M]  pagecounts-2018-10-28.bz2
        ├── [391M]  pagecounts-2018-10-29.bz2
        ├── [389M]  pagecounts-2018-10-30.bz2
        ├── [378M]  pagecounts-2018-10-31.bz2
        ├── [378M]  pagecounts-2018-11-01.bz2
        ├── [376M]  pagecounts-2018-11-02.bz2
        ├── [363M]  pagecounts-2018-11-03.bz2
        ├── [380M]  pagecounts-2018-11-04.bz2
        ├── [394M]  pagecounts-2018-11-05.bz2
        ├── [387M]  pagecounts-2018-11-06.bz2
        ├── [387M]  pagecounts-2018-11-07.bz2
        ├── [380M]  pagecounts-2018-11-08.bz2
        ├── [380M]  pagecounts-2018-11-09.bz2
        ├── [375M]  pagecounts-2018-11-10.bz2
        ├── [396M]  pagecounts-2018-11-11.bz2
        ├── [407M]  pagecounts-2018-11-12.bz2
        ├── [407M]  pagecounts-2018-11-13.bz2
        ├── [418M]  pagecounts-2018-11-14.bz2
        ├── [413M]  pagecounts-2018-11-15.bz2
        ├── [408M]  pagecounts-2018-11-16.bz2
        ├── [383M]  pagecounts-2018-11-17.bz2
        ├── [396M]  pagecounts-2018-11-18.bz2
        ├── [404M]  pagecounts-2018-11-19.bz2
        ├── [402M]  pagecounts-2018-11-20.bz2
        ├── [389M]  pagecounts-2018-11-21.bz2
        ├── [385M]  pagecounts-2018-11-22.bz2
        ├── [380M]  pagecounts-2018-11-23.bz2
        ├── [362M]  pagecounts-2018-11-24.bz2
        ├── [380M]  pagecounts-2018-11-25.bz2
        ├── [398M]  pagecounts-2018-11-26.bz2
        ├── [397M]  pagecounts-2018-11-27.bz2
        ├── [400M]  pagecounts-2018-11-28.bz2
        ├── [395M]  pagecounts-2018-11-29.bz2
        ├── [379M]  pagecounts-2018-11-30.bz2
        ├── [365M]  pagecounts-2018-12-01.bz2
        ├── [377M]  pagecounts-2018-12-02.bz2
        ├── [393M]  pagecounts-2018-12-03.bz2
        ├── [395M]  pagecounts-2018-12-04.bz2
        ├── [408M]  pagecounts-2018-12-05.bz2
        ├── [405M]  pagecounts-2018-12-06.bz2
        ├── [399M]  pagecounts-2018-12-07.bz2
        ├── [396M]  pagecounts-2018-12-08.bz2
        ├── [414M]  pagecounts-2018-12-09.bz2
        ├── [416M]  pagecounts-2018-12-10.bz2
        ├── [407M]  pagecounts-2018-12-11.bz2
        ├── [388M]  pagecounts-2018-12-12.bz2
        ├── [394M]  pagecounts-2018-12-13.bz2
        ├── [381M]  pagecounts-2018-12-14.bz2
        ├── [375M]  pagecounts-2018-12-15.bz2
        ├── [395M]  pagecounts-2018-12-16.bz2
        ├── [399M]  pagecounts-2018-12-17.bz2
        ├── [396M]  pagecounts-2018-12-18.bz2
        ├── [398M]  pagecounts-2018-12-19.bz2
        ├── [389M]  pagecounts-2018-12-20.bz2
        ├── [383M]  pagecounts-2018-12-21.bz2
        ├── [374M]  pagecounts-2018-12-22.bz2
        ├── [365M]  pagecounts-2018-12-23.bz2
        ├── [377M]  pagecounts-2018-12-24.bz2
        ├── [368M]  pagecounts-2018-12-25.bz2
        ├── [382M]  pagecounts-2018-12-26.bz2
        ├── [385M]  pagecounts-2018-12-27.bz2
        ├── [382M]  pagecounts-2018-12-28.bz2
        ├── [379M]  pagecounts-2018-12-29.bz2
        ├── [384M]  pagecounts-2018-12-30.bz2
        ├── [375M]  pagecounts-2018-12-31.bz2
        ├── [379M]  pagecounts-2019-01-01.bz2
        ├── [400M]  pagecounts-2019-01-02.bz2
        ├── [398M]  pagecounts-2019-01-03.bz2
        ├── [384M]  pagecounts-2019-01-04.bz2
        ├── [383M]  pagecounts-2019-01-05.bz2
        ├── [400M]  pagecounts-2019-01-06.bz2
        ├── [396M]  pagecounts-2019-01-07.bz2
        ├── [405M]  pagecounts-2019-01-08.bz2
        ├── [406M]  pagecounts-2019-01-09.bz2
        ├── [395M]  pagecounts-2019-01-10.bz2
        ├── [393M]  pagecounts-2019-01-11.bz2
        ├── [387M]  pagecounts-2019-01-12.bz2
        ├── [397M]  pagecounts-2019-01-13.bz2
        ├── [409M]  pagecounts-2019-01-14.bz2
        ├── [416M]  pagecounts-2019-01-15.bz2
        ├── [426M]  pagecounts-2019-01-16.bz2
        ├── [427M]  pagecounts-2019-01-17.bz2
        ├── [416M]  pagecounts-2019-01-18.bz2
        ├── [395M]  pagecounts-2019-01-19.bz2
        ├── [406M]  pagecounts-2019-01-20.bz2
        ├── [412M]  pagecounts-2019-01-21.bz2
        ├── [406M]  pagecounts-2019-01-22.bz2
        ├── [416M]  pagecounts-2019-01-23.bz2
        ├── [421M]  pagecounts-2019-01-24.bz2
        ├── [410M]  pagecounts-2019-01-25.bz2
        ├── [396M]  pagecounts-2019-01-26.bz2
        ├── [405M]  pagecounts-2019-01-27.bz2
        ├── [411M]  pagecounts-2019-01-28.bz2
        ├── [418M]  pagecounts-2019-01-29.bz2
        ├── [422M]  pagecounts-2019-01-30.bz2
        ├── [408M]  pagecounts-2019-01-31.bz2
        ├── [393M]  pagecounts-2019-02-01.bz2
        ├── [385M]  pagecounts-2019-02-02.bz2
        ├── [398M]  pagecounts-2019-02-03.bz2
        ├── [404M]  pagecounts-2019-02-04.bz2
        ├── [400M]  pagecounts-2019-02-05.bz2
        ├── [397M]  pagecounts-2019-02-06.bz2
        ├── [398M]  pagecounts-2019-02-07.bz2
        ├── [398M]  pagecounts-2019-02-08.bz2
        ├── [380M]  pagecounts-2019-02-09.bz2
        ├── [399M]  pagecounts-2019-02-10.bz2
        ├── [407M]  pagecounts-2019-02-11.bz2
        ├── [405M]  pagecounts-2019-02-12.bz2
        ├── [411M]  pagecounts-2019-02-13.bz2
        ├── [399M]  pagecounts-2019-02-14.bz2
        ├── [397M]  pagecounts-2019-02-15.bz2
        ├── [384M]  pagecounts-2019-02-16.bz2
        ├── [396M]  pagecounts-2019-02-17.bz2
        ├── [407M]  pagecounts-2019-02-18.bz2
        ├── [415M]  pagecounts-2019-02-19.bz2
        ├── [412M]  pagecounts-2019-02-20.bz2
        ├── [407M]  pagecounts-2019-02-21.bz2
        ├── [399M]  pagecounts-2019-02-22.bz2
        ├── [385M]  pagecounts-2019-02-23.bz2
        ├── [394M]  pagecounts-2019-02-24.bz2
        ├── [412M]  pagecounts-2019-02-25.bz2
        ├── [410M]  pagecounts-2019-02-26.bz2
        ├── [407M]  pagecounts-2019-02-27.bz2
        ├── [403M]  pagecounts-2019-02-28.bz2
        ├── [392M]  pagecounts-2019-03-01.bz2
        ├── [383M]  pagecounts-2019-03-02.bz2
        ├── [398M]  pagecounts-2019-03-03.bz2
        ├── [402M]  pagecounts-2019-03-04.bz2
        ├── [405M]  pagecounts-2019-03-05.bz2
        ├── [400M]  pagecounts-2019-03-06.bz2
        ├── [395M]  pagecounts-2019-03-07.bz2
        ├── [376M]  pagecounts-2019-03-08.bz2
        ├── [381M]  pagecounts-2019-03-09.bz2
        ├── [393M]  pagecounts-2019-03-10.bz2
        ├── [400M]  pagecounts-2019-03-11.bz2
        ├── [401M]  pagecounts-2019-03-12.bz2
        ├── [401M]  pagecounts-2019-03-13.bz2
        ├── [398M]  pagecounts-2019-03-14.bz2
        ├── [379M]  pagecounts-2019-03-15.bz2
        ├── [372M]  pagecounts-2019-03-16.bz2
        ├── [393M]  pagecounts-2019-03-17.bz2
        ├── [410M]  pagecounts-2019-03-18.bz2
        ├── [412M]  pagecounts-2019-03-19.bz2
        ├── [405M]  pagecounts-2019-03-20.bz2
        ├── [399M]  pagecounts-2019-03-21.bz2
        ├── [401M]  pagecounts-2019-03-22.bz2
        ├── [389M]  pagecounts-2019-03-23.bz2
        ├── [396M]  pagecounts-2019-03-24.bz2
        ├── [408M]  pagecounts-2019-03-25.bz2
        ├── [408M]  pagecounts-2019-03-26.bz2
        ├── [403M]  pagecounts-2019-03-27.bz2
        ├── [402M]  pagecounts-2019-03-28.bz2
        ├── [391M]  pagecounts-2019-03-29.bz2
        ├── [380M]  pagecounts-2019-03-30.bz2
        ├── [392M]  pagecounts-2019-03-31.bz2
        ├── [400M]  pagecounts-2019-04-01.bz2
        ├── [398M]  pagecounts-2019-04-02.bz2
        ├── [403M]  pagecounts-2019-04-03.bz2
        ├── [409M]  pagecounts-2019-04-04.bz2
        ├── [397M]  pagecounts-2019-04-05.bz2
        ├── [379M]  pagecounts-2019-04-06.bz2
        ├── [395M]  pagecounts-2019-04-07.bz2
        ├── [417M]  pagecounts-2019-04-08.bz2
        ├── [410M]  pagecounts-2019-04-09.bz2
        ├── [400M]  pagecounts-2019-04-10.bz2
        ├── [400M]  pagecounts-2019-04-11.bz2
        ├── [392M]  pagecounts-2019-04-12.bz2
        ├── [381M]  pagecounts-2019-04-13.bz2
        ├── [394M]  pagecounts-2019-04-14.bz2
        ├── [398M]  pagecounts-2019-04-15.bz2
        ├── [401M]  pagecounts-2019-04-16.bz2
        ├── [420M]  pagecounts-2019-04-17.bz2
        ├── [396M]  pagecounts-2019-04-18.bz2
        ├── [385M]  pagecounts-2019-04-19.bz2
        ├── [371M]  pagecounts-2019-04-20.bz2
        ├── [380M]  pagecounts-2019-04-21.bz2
        ├── [398M]  pagecounts-2019-04-22.bz2
        ├── [405M]  pagecounts-2019-04-23.bz2
        ├── [407M]  pagecounts-2019-04-24.bz2
        ├── [401M]  pagecounts-2019-04-25.bz2
        ├── [404M]  pagecounts-2019-04-26.bz2
        ├── [396M]  pagecounts-2019-04-27.bz2
        ├── [398M]  pagecounts-2019-04-28.bz2
        ├── [406M]  pagecounts-2019-04-29.bz2
        ├── [398M]  pagecounts-2019-04-30.bz2
        ├── [403M]  pagecounts-2019-05-01.bz2
        ├── [400M]  pagecounts-2019-05-02.bz2
        ├── [396M]  pagecounts-2019-05-03.bz2
        ├── [389M]  pagecounts-2019-05-04.bz2
        ├── [402M]  pagecounts-2019-05-05.bz2
        ├── [406M]  pagecounts-2019-05-06.bz2
        ├── [401M]  pagecounts-2019-05-07.bz2
        ├── [408M]  pagecounts-2019-05-08.bz2
        ├── [391M]  pagecounts-2019-05-09.bz2
        ├── [384M]  pagecounts-2019-05-10.bz2
        ├── [372M]  pagecounts-2019-05-11.bz2
        ├── [384M]  pagecounts-2019-05-12.bz2
        ├── [398M]  pagecounts-2019-05-13.bz2
        ├── [402M]  pagecounts-2019-05-14.bz2
        ├── [394M]  pagecounts-2019-05-15.bz2
        ├── [403M]  pagecounts-2019-05-16.bz2
        ├── [377M]  pagecounts-2019-05-17.bz2
        ├── [362M]  pagecounts-2019-05-18.bz2
        ├── [376M]  pagecounts-2019-05-19.bz2
        ├── [394M]  pagecounts-2019-05-20.bz2
        ├── [390M]  pagecounts-2019-05-21.bz2
        ├── [388M]  pagecounts-2019-05-22.bz2
        ├── [384M]  pagecounts-2019-05-23.bz2
        ├── [369M]  pagecounts-2019-05-24.bz2
        ├── [355M]  pagecounts-2019-05-25.bz2
        ├── [369M]  pagecounts-2019-05-26.bz2
        ├── [386M]  pagecounts-2019-05-27.bz2
        ├── [393M]  pagecounts-2019-05-28.bz2
        ├── [382M]  pagecounts-2019-05-29.bz2
        ├── [375M]  pagecounts-2019-05-30.bz2
        ├── [364M]  pagecounts-2019-05-31.bz2
        ├── [348M]  pagecounts-2019-06-01.bz2
        ├── [362M]  pagecounts-2019-06-02.bz2
        ├── [381M]  pagecounts-2019-06-03.bz2
        ├── [380M]  pagecounts-2019-06-04.bz2
        ├── [392M]  pagecounts-2019-06-05.bz2
        ├── [380M]  pagecounts-2019-06-06.bz2
        ├── [376M]  pagecounts-2019-06-07.bz2
        ├── [362M]  pagecounts-2019-06-08.bz2
        ├── [372M]  pagecounts-2019-06-09.bz2
        ├── [385M]  pagecounts-2019-06-10.bz2
        ├── [386M]  pagecounts-2019-06-11.bz2
        ├── [389M]  pagecounts-2019-06-12.bz2
        ├── [387M]  pagecounts-2019-06-13.bz2
        ├── [372M]  pagecounts-2019-06-14.bz2
        ├── [359M]  pagecounts-2019-06-15.bz2
        ├── [371M]  pagecounts-2019-06-16.bz2
        ├── [386M]  pagecounts-2019-06-17.bz2
        ├── [380M]  pagecounts-2019-06-18.bz2
        ├── [378M]  pagecounts-2019-06-19.bz2
        ├── [374M]  pagecounts-2019-06-20.bz2
        ├── [366M]  pagecounts-2019-06-21.bz2
        ├── [349M]  pagecounts-2019-06-22.bz2
        ├── [362M]  pagecounts-2019-06-23.bz2
        ├── [375M]  pagecounts-2019-06-24.bz2
        ├── [378M]  pagecounts-2019-06-25.bz2
        ├── [369M]  pagecounts-2019-06-26.bz2
        ├── [357M]  pagecounts-2019-06-27.bz2
        ├── [348M]  pagecounts-2019-06-28.bz2
        ├── [337M]  pagecounts-2019-06-29.bz2
        ├── [353M]  pagecounts-2019-06-30.bz2
        ├── [365M]  pagecounts-2019-07-01.bz2
        ├── [370M]  pagecounts-2019-07-02.bz2
        ├── [366M]  pagecounts-2019-07-03.bz2
        ├── [371M]  pagecounts-2019-07-04.bz2
        ├── [369M]  pagecounts-2019-07-05.bz2
        ├── [370M]  pagecounts-2019-07-06.bz2
        ├── [379M]  pagecounts-2019-07-07.bz2
        ├── [395M]  pagecounts-2019-07-08.bz2
        ├── [387M]  pagecounts-2019-07-09.bz2
        ├── [388M]  pagecounts-2019-07-10.bz2
        ├── [382M]  pagecounts-2019-07-11.bz2
        ├── [375M]  pagecounts-2019-07-12.bz2
        ├── [365M]  pagecounts-2019-07-13.bz2
        ├── [370M]  pagecounts-2019-07-14.bz2
        ├── [386M]  pagecounts-2019-07-15.bz2
        ├── [386M]  pagecounts-2019-07-16.bz2
        ├── [387M]  pagecounts-2019-07-17.bz2
        ├── [384M]  pagecounts-2019-07-18.bz2
        ├── [375M]  pagecounts-2019-07-19.bz2
        ├── [355M]  pagecounts-2019-07-20.bz2
        ├── [366M]  pagecounts-2019-07-21.bz2
        ├── [381M]  pagecounts-2019-07-22.bz2
        ├── [374M]  pagecounts-2019-07-23.bz2
        ├── [376M]  pagecounts-2019-07-24.bz2
        ├── [369M]  pagecounts-2019-07-25.bz2
        ├── [353M]  pagecounts-2019-07-26.bz2
        ├── [348M]  pagecounts-2019-07-27.bz2
        ├── [360M]  pagecounts-2019-07-28.bz2
        ├── [371M]  pagecounts-2019-07-29.bz2
        ├── [379M]  pagecounts-2019-07-30.bz2
        ├── [376M]  pagecounts-2019-07-31.bz2
        ├── [374M]  pagecounts-2019-08-01.bz2
        ├── [375M]  pagecounts-2019-08-02.bz2
        ├── [365M]  pagecounts-2019-08-03.bz2
        ├── [369M]  pagecounts-2019-08-04.bz2
        ├── [375M]  pagecounts-2019-08-05.bz2
        ├── [378M]  pagecounts-2019-08-06.bz2
        ├── [380M]  pagecounts-2019-08-07.bz2
        ├── [383M]  pagecounts-2019-08-08.bz2
        ├── [378M]  pagecounts-2019-08-09.bz2
        ├── [372M]  pagecounts-2019-08-10.bz2
        ├── [366M]  pagecounts-2019-08-11.bz2
        ├── [393M]  pagecounts-2019-08-12.bz2
        ├── [386M]  pagecounts-2019-08-13.bz2
        ├── [371M]  pagecounts-2019-08-14.bz2
        ├── [372M]  pagecounts-2019-08-15.bz2
        ├── [364M]  pagecounts-2019-08-16.bz2
        ├── [358M]  pagecounts-2019-08-17.bz2
        ├── [369M]  pagecounts-2019-08-18.bz2
        ├── [385M]  pagecounts-2019-08-19.bz2
        ├── [395M]  pagecounts-2019-08-20.bz2
        ├── [384M]  pagecounts-2019-08-21.bz2
        ├── [388M]  pagecounts-2019-08-22.bz2
        ├── [377M]  pagecounts-2019-08-23.bz2
        ├── [360M]  pagecounts-2019-08-24.bz2
        ├── [378M]  pagecounts-2019-08-25.bz2
        ├── [388M]  pagecounts-2019-08-26.bz2
        ├── [392M]  pagecounts-2019-08-27.bz2
        ├── [390M]  pagecounts-2019-08-28.bz2
        ├── [391M]  pagecounts-2019-08-29.bz2
        ├── [386M]  pagecounts-2019-08-30.bz2
        ├── [366M]  pagecounts-2019-08-31.bz2
        ├── [375M]  pagecounts-2019-09-01.bz2
        ├── [379M]  pagecounts-2019-09-02.bz2
        ├── [394M]  pagecounts-2019-09-03.bz2
        ├── [375M]  pagecounts-2019-09-04.bz2
        ├── [381M]  pagecounts-2019-09-05.bz2
        └── [359M]  pagecounts-2019-09-06.bz2

18 directories, 1374 files
```
