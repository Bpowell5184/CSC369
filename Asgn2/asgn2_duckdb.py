import duckdb

file_path = 'processed_canvas.parquet'

#duckdb.read_parquet('processed_canvas.parquet')

duckdb.sql(f"SELECT * FROM '{file_path}'")