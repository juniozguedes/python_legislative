"""
1. For every legislatorin the dataset, how many bills did the legislator support (voted forthe
bill)? How many bills did the legislator oppose? ( legislators-support-oppose-count.csv)
2. For every bill in the dataset, how many legislators supported the bill? How many legislators
opposed the bill? Who was the primary sponsor of the bill?
"""
import pandas as pd

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
    result_df.to_csv('legislators-support-oppose-count.csv')


def bill_supported_oppose():
    vote_results = pd.read_csv('vote_results.csv')
    legislators = pd.read_csv('legislators.csv')
    bills = pd.read_csv('bills.csv')
    votes  = pd.read_csv('votes.csv')

    result_df = bills.merge(votes.rename(columns={"id": "vote_id"}), left_on="id", right_on="bill_id") \
                    .merge(vote_results.rename(columns={"vote_id": "vote_id2"}).drop("id", axis=1), left_on="vote_id", right_on="vote_id2") \
                    .groupby(["id","title"]) \
                    .apply(lambda x: pd.Series({
                        "supporter_count": len([v for v in x.vote_type if v==1]),
                        "opposer_count": len([v for v in x.vote_type if v==2]),
                        })) \
                    .reset_index()

    # Print the results
    print(result_df)
    result_df.to_csv('bills-support-oppose-count.csv')



def core():
    print("How many Bills Legislator supported and oppose")
    legislator_supported_oppose()

    print("How many Legislators supported and oppose each Bill")
    bill_supported_oppose()

    return True

if __name__ == "__main__":
    print("Starting the program")
    core()