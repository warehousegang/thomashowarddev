"""Reproduce the essay's fictional examples; no business data or fitted ML model.

Dependencies used: matplotlib==3.10.7, numpy==2.5.4.
Run from any directory: python3 generate_figures.py
"""
from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

OUT = Path(__file__).resolve().parent
BG, TEXT, MUTED, GRID = '#12121c', '#e7e7ef', '#aaaabb', '#323242'
GREEN, BLUE, ORANGE = '#00ed64', '#66c8ee', '#f0b66a'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'path',
                     'svg.hashsalt': 'thomas-calculator-essay', 'axes.unicode_minus': False})

def setup(mobile, ylabel):
    fig, ax = plt.subplots(figsize=(3.6, 4.25) if mobile else (7.9, 4.45), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    fig.subplots_adjust(left=.18 if mobile else .105, right=.95 if mobile else .975,
                        top=.87, bottom=.23 if mobile else .20)
    for side in ['top', 'right']: ax.spines[side].set_visible(False)
    for side in ['bottom', 'left']: ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=9 if mobile else 10, length=0, pad=8)
    ax.set_ylabel(ylabel, color=MUTED, fontsize=9 if mobile else 10, labelpad=10)
    ax.grid(axis='y', color=GRID, linewidth=.6, alpha=.65)
    ax.set_axisbelow(True)
    fig.text(.18 if mobile else .105, .955, 'ILLUSTRATIVE EXAMPLE', color=MUTED,
             fontsize=8, fontfamily='DejaVu Sans Mono', va='top')
    return fig, ax

def save(fig, slug, mobile):
    suffix = '-mobile' if mobile else ''
    fig.savefig(OUT / f'{slug}{suffix}.svg', metadata={'Date': None, 'Creator': 'Thomas Howard — illustrative article figures'})
    plt.close(fig)

def csv_file(name, fields, rows):
    with (OUT/name).open('w', newline='') as f:
        writer = csv.writer(f); writer.writerow(fields); writer.writerows(rows)

guests = np.arange(20, 261)
servers = np.ceil(guests/20).astype(int)
csv_file('staffing.csv', ['guests', 'assumed_guests_per_server', 'servers'], zip(guests, np.full(len(guests),20), servers))

rng = np.random.default_rng(180)
means = np.array([40,45,50,55,80,95,55])
dispersion = 25
history = rng.negative_binomial(dispersion, dispersion/(dispersion+np.tile(means,4)))
draws = rng.negative_binomial(dispersion, dispersion/(dispersion+means), size=(100000,7))
low, high = np.quantile(draws, [.1,.9], axis=0)
csv_file('turkey-demand.csv', ['day_index','phase','synthetic_sales','forecast_mean','toy_80pct_lower','toy_80pct_upper'],
         [(i+1,'synthetic_history',int(y),'','','') for i,y in enumerate(history)] +
         [(i+29,'toy_forecast','',int(m),int(lo),int(hi)) for i,(m,lo,hi) in enumerate(zip(means,low,high))])

demand = np.array([75,90,105,120,135])
prob = np.array([.1,.2,.4,.2,.1])
q = np.arange(60,151)
shortage = (np.maximum(demand[None,:]-q[:,None],0)*prob).sum(axis=1)*6
surplus = (np.maximum(q[:,None]-demand[None,:],0)*prob).sum(axis=1)*2
total = shortage+surplus
best = int(q[np.argmin(total)])
assert means.sum()==420 and means.sum()*4/16==105
assert int(np.ceil(180/20))==9
assert abs(np.dot(demand,prob)-105)<1e-9 and best==120
assert abs(total[q==120][0]-42)<1e-9 and abs(total[q==105][0]-48)<1e-9
csv_file('inventory-scenarios.csv',['weekly_usable_demand_lb','probability'],zip(demand,prob))
csv_file('inventory-cost.csv',['usable_stock_target_lb','expected_shortage_penalty_usd','expected_surplus_penalty_usd','expected_total_penalty_usd'],zip(q,np.round(shortage,2),np.round(surplus,2),np.round(total,2)))

for mobile in (False,True):
    fig,ax = setup(mobile,'Serving staff (people)')
    ax.step(guests,servers,where='pre',color=GREEN,linewidth=2.3)
    ax.fill_between(guests,servers,step='pre',color=GREEN,alpha=.055)
    ax.vlines(180,0,9,color=MUTED,linewidth=.8,linestyle=(0,(3,4)))
    ax.scatter([180],[9],s=65,color=GREEN,edgecolors=BG,linewidth=2,zorder=5)
    ax.annotate('180 guests\n9 servers',xy=(180,9),xytext=(70,11.6),color=TEXT,
                fontsize=11,ha='left',va='center',arrowprops={'arrowstyle':'-','color':MUTED,'lw':.8})
    ax.set_xlim(20,260);ax.set_ylim(0,14)
    ax.set_xticks([20,80,140,200,260] if mobile else [20,60,100,140,180,220,260])
    ax.set_yticks([0,3,6,9,12])
    ax.set_xlabel('Guests',color=MUTED,fontsize=10,labelpad=12)
    fig.text(.18 if mobile else .105,.055,'Assumption: 1 server per 20 guests',color=MUTED,fontsize=8 if mobile else 9)
    save(fig,'banquet-staffing',mobile)

    fig,ax=setup(mobile,'Turkey subs (per day)')
    if mobile: fig.subplots_adjust(bottom=.34)
    x=np.arange(28);xf=np.arange(28,35)
    ax.plot(x,history,color=BLUE,linewidth=1.5,marker='o',markersize=2.7,label='Synthetic history')
    ax.plot(xf,means,color=GREEN,linewidth=2,marker='o',markersize=3.5,label='Toy forecast mean')
    ax.fill_between(xf,low,high,color=GREEN,alpha=.16,label='Toy 80% interval')
    ax.axvline(27.5,color=MUTED,linestyle=(0,(3,4)),linewidth=.9)
    ax.set_xlim(-.7,34.7);ax.set_ylim(0,max(150,int(max(high.max(),history.max())+15)))
    ax.set_yticks([0,50,100,150])
    ax.set_xticks([3,17,31] if mobile else [3,10,17,24,31])
    ax.set_xticklabels(['Week 1','Week 3','Next\nweek'] if mobile else ['Week 1','Week 2','Week 3','Week 4','Next week'])
    ax.legend(loc='upper left',bbox_to_anchor=(0,-.24 if mobile else -.22),ncols=1 if mobile else 3,
              frameon=False,labelcolor=MUTED,fontsize=7.6 if mobile else 8,handlelength=1.8,columnspacing=1.1,borderaxespad=0)
    save(fig,'turkey-demand',mobile)

    fig,ax=setup(mobile,'Expected penalty ($ / week)')
    fig.subplots_adjust(bottom=.29 if mobile else .27)
    ax.plot(q,shortage,color=ORANGE,linewidth=1.5,label='Shortage')
    ax.plot(q,surplus,color=BLUE,linewidth=1.5,label='Surplus')
    ax.plot(q,total,color=GREEN,linewidth=2.6,label='Combined')
    ax.vlines(120,0,42,color=MUTED,linewidth=.8,linestyle=(0,(3,4)))
    ax.scatter([120],[42],s=55,color=GREEN,edgecolors=BG,linewidth=1.5,zorder=5)
    ax.annotate('Lowest penalty\n120 lb · $42',xy=(120,42),xytext=(105,190),ha='center',color=TEXT,
                fontsize=10,arrowprops={'arrowstyle':'-','color':MUTED,'lw':.8})
    ax.set_xlim(60,150);ax.set_ylim(0,300)
    ax.set_xticks([60,90,120,150]);ax.set_yticks([0,100,200,300])
    ax.set_xlabel('Usable stock target (lb)',color=MUTED,fontsize=9 if mobile else 10,labelpad=12)
    ax.legend(loc='upper left',bbox_to_anchor=(0,-.28),ncols=3,frameon=False,labelcolor=MUTED,
              fontsize=7.5 if mobile else 9,handlelength=1.7,columnspacing=1,borderaxespad=0)
    save(fig,'inventory-tradeoff',mobile)

print(f'Created six responsive SVG figures and four CSV datasets in {OUT}')
print('Daily illustrative interval bounds:',low.astype(int).tolist(),high.astype(int).tolist())
