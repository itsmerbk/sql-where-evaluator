ops = {"=": lambda a,b: a == b, ">": lambda a,b: a > b, "<": lambda a,b: a < b}

def filter_rows(rows, clauses):
    return [r for r in rows if all(ops[op](r[col], val) for col, op, val in clauses)]

if __name__ == "__main__":
    data = [{"dept": "CSE", "cgpa": 8.53}, {"dept": "ECE", "cgpa": 7.9}]
    assert len(filter_rows(data, [("dept", "=", "CSE"), ("cgpa", ">", 8.0)])) == 1
    print("[PASS] 050_sql_where_evaluator")
