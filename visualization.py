import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('charts', exist_ok=True)

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from CSV."""
    df = pd.read_csv(file_path)
    print("Columns found in CSV:", df.columns.tolist())
    return df

def plot_top_genres(df: pd.DataFrame, output_file: str = "charts/chart1_top_genres.png") -> None:
    """Plot Top 10 Genres."""
    if 'Genre' in df.columns:
        plt.figure(figsize=(10, 5))
        # Genre me multiple hote hain "Action, Drama" isko split karna pare ga
        all_genres = df['Genre'].str.split(', ').explode()
        top_genres = all_genres.value_counts().head(10)
        top_genres.plot(kind='bar', color='lightgreen')
        plt.title('Top 10 Genres', fontsize=14, fontweight='bold')
        plt.xlabel('Genre')
        plt.ylabel('Number of Movies')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
        print(f'✅ Chart 1 saved: {output_file}')
    else:
        print('⚠️ "Genre" column nahi mili')

def plot_rating_distribution(df: pd.DataFrame, output_file: str = "charts/chart2_rating_dist.png") -> None:
    """Plot IMDB Rating Distribution."""
    if 'IMDB_Rating' in df.columns:
        plt.figure(figsize=(8, 5))
        plt.hist(df['IMDB_Rating'].dropna(), bins=20, color='gold', edgecolor='black')
        plt.title('IMDB Rating Distribution', fontsize=14, fontweight='bold')
        plt.xlabel('IMDB Rating')
        plt.ylabel('Number of Movies')
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
        print(f'✅ Chart 2 saved: {output_file}')
    else:
        print('⚠️ "IMDB_Rating" column nahi mili')

def plot_release_year(df: pd.DataFrame, output_file: str = "charts/chart3_release_year.png") -> None:
    """Plot Release Year Distribution."""
    if 'Released_Year' in df.columns:
        plt.figure(figsize=(8, 5))
        plt.hist(df['Released_Year'].dropna(), bins=30, color='lightcoral', edgecolor='black')
        plt.title('Release Year Distribution', fontsize=14, fontweight='bold')
        plt.xlabel('Year')
        plt.ylabel('Number of Movies')
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
        print(f'✅ Chart 3 saved: {output_file}')
    else:
        print('⚠️ "Released_Year" column nahi mili')

def main():
    df = load_data('imdb_top_1000.csv')
    
    plot_top_genres(df)
    plot_rating_distribution(df)
    plot_release_year(df)
    
    print('\nDONE! Check "charts" folder for 3 PNG files')

if __name__ == "__main__":
    main()