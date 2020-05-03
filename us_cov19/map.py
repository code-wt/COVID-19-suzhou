from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Collector, Faker
from pyecharts.datasets import register_url
import pandas as pd

# x_data = ["工业园区", "太仓市", "常熟市", "相城区", "吴江区","姑苏区","吴中区","昆山市","高新区"]
# y_data = data_are
# data_pair = [list(z) for z in zip(x_data, y_data)]
# 如果出现 ssl 异常再加下面这两行
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
data=pd.read_csv('data.csv')
state=pd.read_csv('data.csv',usecols=[0])
print(state.iloc[1,0])
print(state)
positive_number=pd.read_csv('data.csv',usecols=[1])
#print(state)
STATE=[]
POSITIVE_NUMBER=[]
for i in range(len(state)):
    STATE.append(state.iloc[i,0])
    POSITIVE_NUMBER.append(positive_number.iloc[i,0])
data_pair=[list(z) for z in zip(STATE, POSITIVE_NUMBER)]
print(data_pair)
# print((positive_number.iloc[1,0]))
# data_pair = [list(z) for z in zip(state.iloc[1,0], positive_number.iloc[1,0])]
# print(data_pair)
register_url("https://echarts-maps.github.io/echarts-countries-js/")
c = (
    Map()
    .add("核酸监测阳性",[['Alaska', 300], ['Alabama', 4404], ['Arkansas', 1620], ['Arizona', 4234], ['California', 26182], ['colorado', 8675], ['Connecticut', 15884], ['Washington.D.C', 2350], ['Delaware', 2075], ['Florida', 23340], ['Georgia', 16368], ['Hawaii', 541], ['Iowa', 2141], ['Idaho', 1609], ['Illinois', 25733], ['Indiana', 9542], ['Kansas', 1588], ['Kentucky', 2429], ['Louisiana', 22532], ['Massachusetts', 32181], ['Maryland', 10784], ['Maine', 796], ['Michigan', 29263], ['Minnesota', 1912], ['Missouri', 5111], ['Mississippi', 3624], ['Montana', 415], ['North Carolina', 5465], ['North Dakota', 393], ['Nebraska', 1066], ['New Hampshire', 1211], ['New Jersey', 75317], ['New Mexico', 1597], ['Nevada', 3321], ['New York', 222284], ['Ohio', 8414], ['Oklahoma', 2357], ['Oregon', 1736], ['Pennsylvania', 27735], ['Rhode Island', 3838], ['South Carolina', 3931], ['South Dakota', 1311], ['Tennessee', 6262], ['Texas', 16455], ['Utah', 2683], ['Virginia', 6889], ['Vermont', 768], ['Washington', 11152], ['Wisconsin', 3875], ['West Virginia', 739], ['Wyoming', 296], ['Puerto Rico', 1043], ['AS', 0], ['Guam', 135], ['Northern Mariana Islands', 13], ['US Virgin Islands', 51]], "美国")
    .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    .render()
)
# (
#     Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
#     .add_js_funcs("echarts.registerMap('HK', {});".format(data))
#     .add(
#         series_name="香港18区人口密度",
#         maptype="HK",
#         data_pair=data_pair,
#         name_map=NAME_MAP_DATA,
#         is_map_symbol_show=False,
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(
#             title="香港18区人口密度 （2011）",
#             subtitle="人口密度数据来自Wikipedia",
#             subtitle_link=WIKI_LINK,
#         ),
#         tooltip_opts=opts.TooltipOpts(
#             trigger="item", formatter="{b}<br/>{c} (p / km2)"
#         ),
#         visualmap_opts=opts.VisualMapOpts(
#             min_=800,
#             max_=50000,
#             range_text=["High", "Low"],
#             is_calculable=True,
#             range_color=["lightskyblue", "yellow", "orangered"],
#         ),
#     )
#     .render("population_density_of_HongKong.html")
# )