#Learning Visualisation using Python Libraries (Pandas, Matplotlib and Seaborn)
import pandas as pd
df = pd.DataFrame(np.random.randn(10,4), index=pd.date_range('1/1/2000',periods=10),  columns=list('ABCD'))

