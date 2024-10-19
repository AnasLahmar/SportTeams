import streamlit as st
from streamlit_option_menu import option_menu

# Fonction pour créer les équipes équilibrées
def create_balanced_teams(players):
    sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
    
    team_a = []
    team_b = []
    
    # Alternance des choix pour équilibrer les équipes
    for i, player in enumerate(sorted_players):
        if i % 2 == 0:
            team_a.append(player)
        else:
            team_b.append(player)
    
    # Calcul des scores totaux
    score_a = sum(player[1] for player in team_a)
    score_b = sum(player[1] for player in team_b)

    return team_a, score_a, team_b, score_b


selected=option_menu(
    menu_title="Foot 2 Rue",
    options=["Home","Get Teams"],
    icons=["house","bar-chart"],
    menu_icon="cast",  # optional
    default_index=0,
    orientation="horizontal",  
    styles={
        "nav-link-selected": {"background-color": "#4B9DFF"},
    } 

     )

if selected == "Home":
    st.title("Règles de répartition")
    st.success("Le tirage des équipes se base principalement sur le score de chaque joueur. Il est important de noter que ce score peut varier en fonction de la performance individuelle du joueur lors de chaque match.")
else :
    # Interface utilisateur avec Streamlit
    st.title("Scores des joueurs")
    # Liste des joueurs avec leur score initial
    default_players = [
        ("Saad", 8.5),
        ("Anas", 7),
        ("Badre", 7.5),
        ("Aymen", 7),
        ("Achraf", 8),
        ("Simo", 9),
        ("Rahal", 7.5),
        ("Mohcine", 7),
        ("Labid", 6),
        ("Mohammed CT", 8),
        ("Issam", 9),
        ("Moad", 10),
        ("Nabil capi", 8.5),
        ("Mohammed Tanjawi", 7),
        ("Abdelkrim", 8),
        ("Omar", 8.5)
    ]

    # Liste pour stocker les joueurs et leurs scores mis à jour
    players = []

    # Affichage des joueurs 2 par ligne (8 lignes au total)
    for i in range(0, len(default_players), 2):
        # Créer deux colonnes pour chaque rangée de deux joueurs
        col1, col2 = st.columns(2)
        
        # Premier joueur dans la colonne de gauche
        with col1:
            with st.expander(f"Paramètres du joueur : {default_players[i][0]}", expanded=False):
                name = st.text_input(f"Nom du joueur {default_players[i][0]}", value=default_players[i][0])
                score = st.slider(f"Score de {name}", min_value=1.0, max_value=10.0, value=float(default_players[i][1]), step=0.5)
                players.append((name, score))

        # Deuxième joueur dans la colonne de droite (s'il existe)
        if i + 1 < len(default_players):
            with col2:
                with st.expander(f"Paramètres du joueur : {default_players[i+1][0]}", expanded=False):
                    name = st.text_input(f"Nom du joueur {default_players[i+1][0]}", value=default_players[i+1][0])
                    score = st.slider(f"Score de {name}", min_value=1.0, max_value=10.0, value=float(default_players[i+1][1]), step=0.5)
                    players.append((name, score))


    # Bouton pour générer les équipes
    if st.button("Get Teams"):
        team_a, score_a, team_b, score_b = create_balanced_teams(players)
        
        # Affichage des équipes et des scores
        col1,col2 =st.columns(2)
        col1.subheader("Équipe A")
        for player in team_a:
            col1.write(f"{player[0]}")
        col1.info(f"Score total Équipe A: {score_a}")
        
        col2.subheader("Équipe B")
        for player in team_b:
            col2.write(f"{player[0]}")
        col2.info(f"Score total Équipe B: {score_b}")
