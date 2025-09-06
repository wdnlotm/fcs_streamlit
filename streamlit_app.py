import streamlit as st
import time

st.set_page_config(page_title="high dimensional cytometry", page_icon="🎈")
st.title("🎈 High dimensional cytometry data analysis")

steps = ["Select a step...", "z00", "z01", "z02", "z03", "z04"]
######### Side ##############
# Instructions to run the app
with st.sidebar:
    st.header("FCS analysis")
    st.markdown(
    """
    * There are five steps for the round one.
    1. z00 - explore cofactors hi
    2. z01 - batch correction
    3. z02 - knn & umap
    4. z03 - RAPIDS Leiden
    5. z04 - Pick a clustering
    """)
    selected_step = st.selectbox("Choose a step:", steps)

######### Main ##############
# if st.button("Click me!"):
#     st.write("Button clicked! Performing action...")
#     # Add your desired action code here

st.write(
    "Pick a step using the menu on the left."
)
# selected_option == "Select an option..."
if selected_step == "z00":
    cofactor_list = st.text_input("Cofactors to be applied:", value="[cf*1000.0 for cf in range(1,16)]", max_chars=500)
    st.write(cofactor_list)
    clist = eval(cofactor_list)
    st.code(clist)
    if st.button("Execute"):
        st.write("Start!!")
        with st.spinner("working.."):
            time.sleep(2) 
            st.write(f"Step {selected_step} will show marker density behavior depending on various cofactors. Users need to choose optimal cofactors")
            time.sleep(4) 
            st.image("images/nogroup_spect_marker_CD20_bw_0.5.png", caption="CD20 cofactors")
            time.sleep(4) 
            st.image("images/nogroup_spect_marker_IgD_bw_0.5.png", caption="IgD cofactors")

# if selected_option == "Select an option...":
#     st.write("No option selected yet.")
# elif selected_option == "z00":
#     with st.spinner("working.."):
#         time.sleep(2) 
#         st.write(f"Step {selected_option} will show marker density behavior depending on various cofactors. Users need to choose optimal cofactors")
#         time.sleep(4) 
#         st.image("images/nogroup_spect_marker_CD20_bw_0.5.png", caption="CD20 cofactors")
#         time.sleep(4) 
#         st.image("images/nogroup_spect_marker_IgD_bw_0.5.png", caption="IgD cofactors")
# elif selected_option == "z01":
#     with st.spinner("working.."):
#         time.sleep(2) 
#         st.write(f"Step {selected_option} will perform batch effect correction by deploying CyCombine. An R code is involved.")
#         time.sleep(4) 
#         st.image("images/Pre_batch_correction_markers_w_custom_cofactor_nogroup.png", caption="PRE batch correction")
#         time.sleep(4) 
#         st.image("images/Post_batch_correction_markers_w_custom_cofactor_nogroup.png", caption="POST batch correction")
# elif selected_option == "z02":
#     with st.spinner("working.."):
#         time.sleep(2) 
#         st.write(f"Step {selected_option} will calculate the UMAP projection and the KNN graph edgelist.")
#         time.sleep(4) 
#         st.image("images/umap_density_b_cell_markers.png", caption="UMAP with cell density")
#         time.sleep(4) 
#         st.image("images/umap_markers_b_cell_markers.png", caption="UMAP with clustering marker expressions")
# elif selected_option == "z03":
#     with st.spinner("working.."):
#         time.sleep(2) 
#         st.write(f"Step {selected_option} will perform the Leiden clustering. GPU-based library from RAPIDS will be utilized.")
#         time.sleep(4) 
#         text1 = """ ('computation time = 0:00:19.661074', 'resolution =  0.1')
# <br>('number of cluster = 4', 'modularity score = 0.9303182363510132', 'big enough clusters (>0.5%) = 4', 'big enough cluster total = 100.0')
# <br>partition <br>0 - 51.762528 <br>1 - 28.081759 <br>2 - 14.900670 <br>3 - 5.255043 """
#         st.write(text1,unsafe_allow_html=True)
#         text2 = """ <br>('computation time = 0:00:22.542235', 'resolution =  0.2') <br>
# ('number of cluster = 5', 'modularity score = 0.9076583981513977', 'big enough clusters (>0.5%) = 5', 'big enough cluster total = 100.0') <br>
# partition <br> 0 - 30.091424 <br> 1 - 27.072061 <br> 2 - 22.021883 <br> 3 - 15.555258 <br> 4 - 5.259374 """
#         time.sleep(4) 
#         st.write(text2,unsafe_allow_html=True)
#         text3 = """ <br>('computation time = 0:00:15.527664', 'resolution =  0.3')<br>
# ('number of cluster = 7', 'modularity score = 0.8825947046279907', 'big enough clusters (>0.5%) = 6', 'big enough cluster total = 99.60883336830247')
# <br> partition <br>4 - 28.466626 <br>1 - 27.592773 <br>3 - 15.566114 <br>0 - 11.511122 <br>2 - 11.214568 <br>5 - 5.257631 <br>6 - 0.391167"""
#         time.sleep(4) 
#         st.write(text3,unsafe_allow_html=True)
# elif selected_option == "z04":
#     with st.spinner("working.."):
#         time.sleep(2) 
#         st.write(f"Step {selected_option} will examine clustering results to move forward with one.")
#         time.sleep(6) 
#         st.image("images/rp0.100_cluster_umap_b_cell_markers_hogan.png", caption="Cluster UMAP")
#         time.sleep(2) 
#         st.image("images/rp0.100_one_vs_others_b_cell_markers_hogan.png", caption="Cluster overlap")
#         time.sleep(4) 
#         st.image("images/rp0.100_marker_density_by_partition_b_cell_markers_hogan.png", caption="Marker expression by cluster")    

#         time.sleep(6) 
#         st.image("images/rp0.200_cluster_umap_b_cell_markers_hogan.png", caption="Cluster UMAP")
#         time.sleep(2) 
#         st.image("images/rp0.200_one_vs_others_b_cell_markers_hogan.png", caption="Cluster overlap")
#         time.sleep(4) 
#         st.image("images/rp0.200_marker_density_by_partition_b_cell_markers_hogan.png", caption="Marker expression by cluster") 

#         time.sleep(6) 
        st.image("images/rp0.300_cluster_umap_b_cell_markers_hogan.png", caption="Cluster UMAP")
        time.sleep(2) 
        st.image("images/rp0.300_one_vs_others_b_cell_markers_hogan.png", caption="Cluster overlap")
        time.sleep(4) 
        st.image("images/rp0.300_marker_density_by_partition_b_cell_markers_hogan.png", caption="Marker expression by cluster") 
