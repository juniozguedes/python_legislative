"""
1. For every legislatorin the dataset, how many bills did the legislator support (voted forthe
bill)? How many bills did the legislator oppose? ( legislators-support-oppose-count.csv)
2. For every bill in the dataset, how many legislators supported the bill? How many legislators
opposed the bill? Who was the primary sponsor of the bill?
"""
import pandas as pd
from IPython import display

def legislator_supported_oppose():
    vote_results = pd.read_csv('vote_results.csv')
    legislators = pd.read_csv('legislators.csv')
    result_df = legislators.merge(vote_results[["legislator_id","vote_id","vote_type"]], left_on="id", right_on="legislator_id", how="left") \
                       .groupby("id") \
                       .apply(lambda x: pd.Series({
                           "name": str(x["name"].iloc[0]),
                           "num_supported_bills": len([v for v in x.vote_type if v==1]),
                           "num_opposed_bills": len([v for v in x.vote_type if v==2]),
                           })) \
                       .reset_index()

    print(result_df)

def core():
    print("Bills legislator supported and oppose")
    legislator_supported_oppose()
    return True

if __name__ == "__main__":
    print("Starting the program")
    core()