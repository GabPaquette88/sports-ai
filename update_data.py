import json
import datetime
import random

def update_scores():
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    # Mettre à jour les dates
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Mettre à jour les probabilités (exemple)
    for sport in data:
        for game in data[sport]:
            if 'ai_analysis' in game:
                # Ajuster légèrement les probabilités
                game['ai_analysis']['home_win_probability'] = min(95, 
                    game['ai_analysis']['home_win_probability'] + random.randint(-5, 5))
                game['ai_analysis']['confidence'] = min(95,
                    game['ai_analysis']['confidence'] + random.randint(-3, 3))
                
                # Mettre à jour la date
                game['date'] = today
    
    # Sauvegarder
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Données mises à jour le {datetime.datetime.now()}")
    return data

if __name__ == "__main__":
    update_scores()