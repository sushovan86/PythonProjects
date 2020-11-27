from pandas import DataFrame, ExcelWriter


def process_split_sheet(df: DataFrame, column_pick, filename, ext):
    writer = ExcelWriter("{}_split_{}{}".format(filename, column_pick, ext))

    column_values = df[column_pick]
    sorted_column_values = sorted(list(set(column_values)))

    for val in sorted_column_values:
        df.loc[column_values == val] \
            .to_excel(writer,
                      sheet_name=val,
                      index=False,
                      freeze_panes=(1, 0))

    writer.save()
    print('Done')


def process_split_file(df: DataFrame, column_pick, filename, ext):
    column_values = df[column_pick]

    for val in set(column_values):
        df.loc[column_values == val] \
            .to_excel("{}_{}_{}{}".format(filename, column_pick, val, ext),
                      sheet_name=val,
                      index=False,
                      freeze_panes=(1, 0))

    print('Done')
