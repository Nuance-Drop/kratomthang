import os
import re

# Map your current file names to proper data
strains_data = {
    # Format: "filename": {yaml_data}
    "aceh-green": {
        "title": "Aceh Green",
        "category": "Green",
        "type": "Specialty",
        "origin": "Aceh, Sumatra",
        "price_wholesale": 140,
        "price_retail": 280,
        "effects": "Rare, Balanced",
        "featured": "false"
    },
    "aceh-red": {
        "title": "Aceh Red", 
        "category": "Red",
        "type": "Specialty",
        "origin": "Aceh, Sumatra",
        "price_wholesale": 140,
        "price_retail": 280,
        "effects": "Rare, Relaxing",
        "featured": "false"
    },
    "aceh-white": {
        "title": "Aceh White",
        "category": "White", 
        "type": "Specialty",
        "origin": "Aceh, Sumatra",
        "price_wholesale": 140,
        "price_retail": 280,
        "effects": "Rare, Energizing",
        "featured": "false"
    },
    "aceh-yellow": {
        "title": "Aceh Yellow",
        "category": "Gold",
        "type": "Specialty", 
        "origin": "Aceh, Sumatra",
        "price_wholesale": 140,
        "price_retail": 280,
        "effects": "Rare, Smooth",
        "featured": "false"
    },
    "green-maeng-da": {
        "title": "Green Maeng Da",
        "category": "Green",
        "type": "Maeng Da",
        "origin": "Thailand",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Energizing, Focus",
        "featured": "true"
    },
    "red-maeng-da": {
        "title": "Red Maeng Da",
        "category": "Red", 
        "type": "Maeng Da",
        "origin": "Thailand",
        "price_wholesale": 135,
        "price_retail": 260,
        "effects": "Potent, Relaxing",
        "featured": "true"
    },
    "white-maeng-da": {
        "title": "White Maeng Da",
        "category": "White",
        "type": "Maeng Da", 
        "origin": "Thailand",
        "price_wholesale": 135,
        "price_retail": 260,
        "effects": "Stimulating, Focus",
        "featured": "true"
    },
    "super-green": {
        "title": "Super Green",
        "category": "Green",
        "type": "Premium",
        "origin": "Borneo",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Balanced, Long-lasting",
        "featured": "true"
    },
    "green-bali": {
        "title": "Green Bali",
        "category": "Green",
        "type": "Bali",
        "origin": "Indonesia",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Relaxing, Smooth",
        "featured": "false"
    },
    "red-bali": {
        "title": "Red Bali",
        "category": "Red",
        "type": "Bali", 
        "origin": "Indonesia",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Calming, Evening",
        "featured": "true"
    },
    "white-bali": {
        "title": "White Bali",
        "category": "White",
        "type": "Bali",
        "origin": "Indonesia", 
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Mild Energy",
        "featured": "false"
    },
    "green-borneo": {
        "title": "Green Borneo",
        "category": "Green",
        "type": "Borneo",
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Balanced, Clean",
        "featured": "false"
    },
    "red-borneo": {
        "title": "Red Borneo", 
        "category": "Red",
        "type": "Borneo",
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Relaxing, Pain Relief",
        "featured": "false"
    },
    "white-borneo": {
        "title": "White Borneo",
        "category": "White",
        "type": "Borneo", 
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Energy, Focus",
        "featured": "true"
    },
    "green-horn": {
        "title": "Green Horn",
        "category": "Green",
        "type": "Horn",
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Unique, Balanced",
        "featured": "false"
    },
    "red-horn": {
        "title": "Red Horn",
        "category": "Red",
        "type": "Horn",
        "origin": "Borneo", 
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Strong, Relaxing",
        "featured": "false"
    },
    "white-horn": {
        "title": "White Horn",
        "category": "White",
        "type": "Horn",
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Energizing, Uplifting",
        "featured": "false"
    },
    "green-thai": {
        "title": "Green Thai",
        "category": "Green",
        "type": "Thai",
        "origin": "Thailand",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Stimulating, Happy",
        "featured": "false"
    },
    "red-thai": {
        "title": "Red Thai",
        "category": "Red",
        "type": "Thai",
        "origin": "Thailand",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Relaxing, Mood Lift",
        "featured": "false"
    },
    "white-thai": {
        "title": "White Thai",
        "category": "White",
        "type": "Thai", 
        "origin": "Thailand",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Energy, Euphoria",
        "featured": "false"
    },
    "gold-thai": {
        "title": "Gold Thai",
        "category": "Gold",
        "type": "Gold Reserve",
        "origin": "Thailand",
        "price_wholesale": 140,
        "price_retail": 280,
        "effects": "Premium, Smooth",
        "featured": "true"
    },
    "green-malay": {
        "title": "Green Malay",
        "category": "Green",
        "type": "Malay",
        "origin": "Malaysia",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Long-lasting, Euphoric",
        "featured": "false"
    },
    "red-malay": {
        "title": "Red Malay", 
        "category": "Red",
        "type": "Malay",
        "origin": "Malaysia",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Relaxing, Sedating",
        "featured": "false"
    },
    "green-elephant": {
        "title": "Green Elephant",
        "category": "Green",
        "type": "Elephant",
        "origin": "Thailand",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Potent, Unique",
        "featured": "false"
    },
    "red-elephant": {
        "title": "Red Elephant",
        "category": "Red",
        "type": "Elephant", 
        "origin": "Thailand",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Strong, Relaxing",
        "featured": "false"
    },
    "white-elephant": {
        "title": "White Elephant",
        "category": "White",
        "type": "Elephant",
        "origin": "Thailand",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Energizing, Potent",
        "featured": "false"
    },
    "green-dragon": {
        "title": "Green Dragon",
        "category": "Green",
        "type": "Dragon Blend",
        "origin": "Indonesia",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Blend, Balanced",
        "featured": "false"
    },
    "red-dragon": {
        "title": "Red Dragon",
        "category": "Red",
        "type": "Dragon Blend",
        "origin": "Indonesia",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Blend, Relaxing",
        "featured": "false"
    },
    "green-hulu": {
        "title": "Green Hulu Kapuas",
        "category": "Green",
        "type": "Hulu",
        "origin": "Kalimantan",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Rare, Balanced",
        "featured": "false"
    },
    "red-hulu": {
        "title": "Red Hulu Kapuas",
        "category": "Red",
        "type": "Hulu", 
        "origin": "Kalimantan",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Rare, Relaxing",
        "featured": "false"
    },
    "white-hulu": {
        "title": "White Hulu Kapuas",
        "category": "White",
        "type": "Hulu",
        "origin": "Kalimantan",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Rare, Energizing",
        "featured": "false"
    },
    "green-ketapang": {
        "title": "Green Ketapang",
        "category": "Green",
        "type": "Ketapang",
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Smooth, Relaxing",
        "featured": "false"
    },
    "red-ketapang": {
        "title": "Red Ketapang",
        "category": "Red",
        "type": "Ketapang",
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Evening, Calm",
        "featured": "false"
    },
    "white-ketapang": {
        "title": "White Ketapang",
        "category": "White",
        "type": "Ketapang", 
        "origin": "Borneo",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Daytime, Focus",
        "featured": "false"
    },
    "green-sumatra": {
        "title": "Green Sumatra",
        "category": "Green",
        "type": "Sumatra",
        "origin": "Sumatra",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Smooth, Uplifting",
        "featured": "false"
    },
    "red-sumatra": {
        "title": "Red Sumatra",
        "category": "Red",
        "type": "Sumatra",
        "origin": "Sumatra",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Relaxing, Sleep",
        "featured": "false"
    },
    "white-sumatra": {
        "title": "White Sumatra",
        "category": "White",
        "type": "Sumatra",
        "origin": "Sumatra",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Stimulating, Happy",
        "featured": "false"
    },
    "red-bentuangie": {
        "title": "Red Bentuangie",
        "category": "Red",
        "type": "Bentuangie",
        "origin": "Indonesia",
        "price_wholesale": 130,
        "price_retail": 250,
        "effects": "Fermented, Unique",
        "featured": "false"
    },
    "red-vietnam": {
        "title": "Red Vietnam",
        "category": "Red",
        "type": "Vietnam",
        "origin": "Vietnam",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Smooth, Balanced",
        "featured": "false"
    },
    "white-vietnam": {
        "title": "White Vietnam",
        "category": "White",
        "type": "Vietnam", 
        "origin": "Vietnam",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Clean, Energy",
        "featured": "false"
    },
    "yellow-bali": {
        "title": "Yellow Bali",
        "category": "Gold",
        "type": "Yellow",
        "origin": "Indonesia",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Mild, Smooth",
        "featured": "false"
    },
    "yellow-vietnam": {
        "title": "Yellow Vietnam",
        "category": "Gold",
        "type": "Yellow",
        "origin": "Vietnam",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Unique, Balanced",
        "featured": "false"
    },
    "yellow-sumatra": {
        "title": "Yellow Sumatra",
        "category": "Gold",
        "type": "Yellow",
        "origin": "Sumatra",
        "price_wholesale": 125,
        "price_retail": 240,
        "effects": "Smooth, Happy",
        "featured": "false"
    },
    "gold-borneo": {
        "title": "Gold Borneo",
        "category": "Gold",
        "type": "Gold",
        "origin": "Borneo",
        "price_wholesale": 135,
        "price_retail": 270,
        "effects": "Premium, Relaxing",
        "featured": "false"
    },
    "gold-elephant": {
        "title": "Gold Elephant",
        "category": "Gold",
        "type": "Gold",
        "origin": "Thailand",
        "price_wholesale": 140,
        "price_retail": 280,
        "effects": "Premium, Potent",
        "featured": "true"
    },
    "zombie-green": {
        "title": "Zombie Green",
        "category": "Green",
        "type": "Zombie",
        "origin": "Indonesia",
        "price_wholesale": 150,
        "price_retail": 300,
        "effects": "Ultra Potent, Strong",
        "featured": "true"
    },
    "zombie-red": {
        "title": "Zombie Red", 
        "category": "Red",
        "type": "Zombie",
        "origin": "Indonesia",
        "price_wholesale": 150,
        "price_retail": 300,
        "effects": "Ultra Strong, Sedating",
        "featured": "true"
    },
    "zombie-white": {
        "title": "Zombie White",
        "category": "White",
        "type": "Zombie",
        "origin": "Indonesia",
        "price_wholesale": 150,
        "price_retail": 300,
        "effects": "Ultra Potent, Energy",
        "featured": "true"
    },
    "zombie-yellow": {
        "title": "Zombie Yellow",
        "category": "Gold",
        "type": "Zombie",
        "origin": "Indonesia",
        "price_wholesale": 150,
        "price_retail": 300,
        "effects": "Ultra Strong, Balanced",
        "featured": "true"
    }
}

def create_strain_file(slug, data):
    """Create a properly formatted Jekyll strain file"""
    content = f"""---
title: {data['title']}
type: {data['type']}
category: {data['category']}
origin: {data['origin']}
price_wholesale: {data['price_wholesale']}
price_retail: {data['price_retail']}
effects: {data['effects']}
featured: {data['featured']}
layout: strain
---

{data['title']} is a premium {data['category']} vein kratom sourced directly from family farms in {data['origin']}. 

**Effects Profile:** {data['effects']}

This strain is harvested from mature leaves and processed using traditional indoor drying techniques to preserve maximum alkaloid content. Lab-tested for purity and contaminants.

**Batch Notes:** Direct trade, customs cleared under HTS Code 1211.90.8090.
"""
    
    filename = f"_strains/{slug}.md"
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

def main():
    # Ensure _strains directory exists
    if not os.path.exists('_strains'):
        os.makedirs('_strains')
        print("Created _strains directory")
    
    # Create all strain files
    for slug, data in strains_data.items():
        create_strain_file(slug, data)
    
    print(f"\n✅ Created {len(strains_data)} strain files in _strains/")

if __name__ == "__main__":
    main()
