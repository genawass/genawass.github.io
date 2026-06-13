# CVPR 2026 production computer-vision shortlist

The full set behind the readiness chart in [What CVPR 2026 Says About Production Computer Vision](https://genawass.github.io/posts/cvpr2026-production.html).

**14 themes · 84 papers · six papers per theme.**

Grades measure production usefulness, not academic quality. Readiness is `now`, `near`, or `research`.

## 1. Detection, segmentation & visual recognition

**Production scope:** The core perception layer for nearly every vision product.

1. [Exploring Hierarchical Consistency and Unbiased Objectness for Open-Vocabulary Object Detection](https://openaccess.thecvf.com/content/CVPR2026F/html/Lee_Exploring_Hierarchical_Consistency_and_Unbiased_Objectness_for_Open-Vocabulary_Object_Detection_CVPRF_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** Fixes two open-vocabulary failure modes—region-level pseudo-labels VLMs get wrong, and proposals biased toward known classes—so new categories are added by prompt instead of retraining.
2. [MARIS: Marine Open-Vocabulary Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near
   - **Why it matters:** A large-scale benchmark and method for open-vocabulary instance segmentation underwater, where novel marine categories must be recognized without a fixed class list.
3. [AKCMamba-YOLO: Selective State Space Models For Real-Time Object Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_AKCMamba-YOLO_Selective_State_Space_Models_For_Real-Time_Object_Detection_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** L · **Readiness:** now
   - **Why it matters:** Adds state-space (Mamba) modeling to YOLO to capture long-range context while keeping real-time speed—a drop-in efficiency upgrade for existing detectors.
4. [DetRefiner: Model-Agnostic Detection Refinement with Feature Fusion Transformer](https://openaccess.thecvf.com/content/CVPR2026F/html/Okazaki_DetRefiner_Model-Agnostic_Detection_Refinement_with_Feature_Fusion_Transformer_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** A plug-and-play module that fuses global and local features to refine any detector's open-vocabulary predictions on unseen objects.
5. [VLM4RSDet: Collaborative Optimization with Vision-Language Model for Enhancing Remote Sensing Object Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_VLM4RSDet_Collaborative_Optimization_with_Vision-Language_Model_for_Enhancing_Remote_Sensing_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** now
   - **Why it matters:** Uses a vision-language model's priors to push remote-sensing detection accuracy past closed-set limits.
6. [Don't Let the Information Slip Away](https://openaccess.thecvf.com/content/CVPR2026F/html/Li_Dont_Let_the_Information_Slip_Away_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** now
   - **Why it matters:** A YOLO-line refinement that preserves information lost in the feature path, squeezing more accuracy from real-time CNN detectors.

## 2. Video intelligence & persistent tracking

**Production scope:** Products that understand events, motion, and identity over time.

1. [Breaking Smooth-Motion Assumptions: A UAV Benchmark for Multi-Object Tracking in Complex and Adverse Conditions](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_Breaking_Smooth-Motion_Assumptions_A_UAV_Benchmark_for_Multi-Object_Tracking_in_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near · must-read
   - **Why it matters:** A UAV tracking benchmark built around the shake, occlusion, and non-smooth motion existing benchmarks omit—deployment-shaped stress for any tracker, generalist or not.
2. [TLMA: Mitigating the Impact of Weakly Labeled Information for Video Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_TLMA_Mitigating_the_Impact_of_Weakly_Labeled_Information_for_Video_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** L · **Readiness:** near
   - **Why it matters:** Reduces the noise that weak video-level labels inject into anomaly detection, lowering annotation cost without the usual accuracy hit.
3. [TGTrack: Temporal Generative Learning for Unified Single Object Tracking](https://openaccess.thecvf.com/content/CVPR2026/html/Geng_TGTrack_Temporal_Generative_Learning_for_Unified_Single_Object_Tracking_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Adds genuine temporal supervision to single-object tracking through a generative formulation—stronger temporal modeling, still research-stage.
4. [VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition](https://openaccess.thecvf.com/content/CVPR2026/html/Yadav_VideoNet_A_Large-Scale_Dataset_for_Domain-Specific_Action_Recognition_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** near
   - **Why it matters:** A large-scale dataset for domain-specific action recognition—training fuel where generic action models underperform.
5. [Occlusion-Aware SORT: Observing Occlusion for Robust Multi-Object Tracking](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Occlusion-Aware_SORT_Observing_Occlusion_for_Robust_Multi-Object_Tracking_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** now
   - **Why it matters:** A plug-and-play, training-free add-on that makes existing SORT trackers robust to partial occlusion—easy to drop into a deployed MOT pipeline.
6. [Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Clark_Molmo2_Open_Weights_and_Data_for_Vision-Language_Models_with_Video_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** H · **Readiness:** now
   - **Why it matters:** Open weights, data, and recipe for a video-language model with pixel-level pointing and tracking—grounding even proprietary VLMs lack—a reusable base for search, annotation, and operator tooling.

## 3. 3D perception, reconstruction & digital twins

**Production scope:** Spatial understanding for mapping, simulation, inspection, and AR.

1. [V-DPM: 4D Video Reconstruction with Dynamic Point Maps](https://openaccess.thecvf.com/content/CVPR2026/html/Sucar_V-DPM_4D_Video_Reconstruction_with_Dynamic_Point_Maps_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Extends DUSt3R-style point maps to dynamic scenes (motion plus geometry), advancing feed-forward 4D reconstruction—promising but research-stage.
2. [MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_MoRGS_Efficient_Per-Gaussian_Motion_Reasoning_for_Streamable_Dynamic_3D_Scenes_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** L · **Readiness:** now
   - **Why it matters:** Per-Gaussian motion reasoning that makes online 4D reconstruction from streaming multi-view input fast enough for low-latency use.
3. [SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction](https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** Drops the precomputed-pose assumption from Gaussian Splatting, jointly optimizing pose and reconstruction so it survives fast-motion, real-world capture.
4. [Velox: Learning Representations of 4D Geometry and Appearance](https://openaccess.thecvf.com/content/CVPR2026/html/Malik_Velox_Learning_Representations_of_4D_Geometry_and_Appearance_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Learns compact 4D representations from raw dynamic point clouds—descriptive and efficient, but early.
5. [Efficiently Reconstructing Dynamic Scenes One D4RT at a Time](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** One feed-forward transformer with a shared query interface returns depth, pose, tracking, and dynamic reconstruction—several specialized outputs as views of one scene model.
6. [4D Primitive-Mache: Glueing Primitives for Persistent 4D Scene Reconstruction](https://openaccess.thecvf.com/content/CVPR2026/html/Mazur_4D_Primitive-Mache_Glueing_Primitives_for_Persistent_4D_Scene_Reconstruction_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Reconstructs a complete, persistent scene from casual monocular video—including parts no longer in view—so the full scene can be replayed.

## 4. Cross-view, multimodal alignment & registration

**Production scope:** Connecting observations across cameras, sensors, viewpoints, and maps.

1. [C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion](https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** Training-free point-cloud registration that uses generative priors and vision foundation models to generalize across sensors and sampling differences—no per-modality retraining.
2. [RHO: Robust Holistic OSM-Based Metric Cross-View Geo-Localization](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_RHO_Robust_Holistic_OSM-Based_Metric_Cross-View_Geo-Localization_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near
   - **Why it matters:** Metric cross-view geo-localization from panoramas and OpenStreetMap instead of satellite imagery—useful where overhead imagery is unavailable.
3. [DualReg: Dual-Space Filtering and Reinforcement for Rigid Registration](https://openaccess.thecvf.com/content/CVPR2026/html/Li_DualReg_Dual-Space_Filtering_and_Reinforcement_for_Rigid_Registration_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Combines feature-based and geometry-based matching for rigid registration that is both robust to large transforms and locally accurate, in real time.
4. [Generalizable Structure-Aware Keypoint Correspondence for Category-Unified 3D Single Object Tracking](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_Generalizable_Structure-Aware_Keypoint_Correspondence_for_Category-Unified_3D_Single_Object_Tracking_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** near
   - **Why it matters:** One category-unified 3D tracker via keypoint correspondence, replacing the per-class model zoo that limits scalability.
5. [Cross-Instance Gaussian Splatting Registration via Geometry-Aware Feature-Guided Alignment](https://openaccess.thecvf.com/content/CVPR2026/html/Amoyal_Cross-Instance_Gaussian_Splatting_Registration_via_Geometry-Aware_Feature-Guided_Alignment_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Aligns two independent Gaussian-Splatting models even across different instances of a category—registration beyond identical objects, still early.
6. [PAUL: Uncertainty-Guided Partition and Augmentation for Robust Cross-View Geo-Localization under Noisy Correspondence](https://openaccess.thecvf.com/content/CVPR2026/html/Li_PAUL_Uncertainty-Guided_Partition_and_Augmentation_for_Robust_Cross-View_Geo-Localization_under_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Robust cross-view geo-localization under noisy correspondence via uncertainty-guided partitioning—relevant to UAV navigation and aerial surveying.

## 5. Robotics, embodied AI & autonomous systems

**Production scope:** Vision that closes the loop from sensing to physical action.

1. [AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** research
   - **Why it matters:** Gives vision-language-action models visual memory across timesteps, fixing the history-blind Markov assumption that hurts real robot control—research-stage.
2. [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Injects active perception into VLA models so the robot moves to gather the views it needs for precise 3D manipulation—research-stage.
3. [SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** A VLA model that actively chooses what to observe and executes with viewpoint-invariant control—the instruction sets the goal, the model decides part of the procedure.
4. [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](https://openaccess.thecvf.com/content/CVPR2026F/html/Yi_Evolve_Vision-Language-Action_Model_into_an_Agent_with_On-the-fly_Tool-use_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Turns any VLA model into an agent that calls off-the-shelf tools for low-level vision and affordance—tool-use as a robot capability layer.
5. [MM-ACT: Learn from Multimodal Parallel Generation to Act](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** A unified VLA model with text, image, and action in one token space, generating across modalities for planning and control—research-stage.
6. [HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_HiF-VLA_Hindsight_Insight_and_Foresight_through_Motion_Representation_for_Vision-Language-Action_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Adds hindsight/insight/foresight motion representation to break the temporal myopia that degrades long-horizon VLA tasks—research-stage.

## 6. Human understanding, biometrics & interaction

**Production scope:** Vision products centered on people, behavior, and interfaces.

1. [Forecasting 3D Scanpaths in Egocentric Video](https://openaccess.thecvf.com/content/CVPR2026/html/Ryan_Forecasting_3D_Scanpaths_in_Egocentric_Video_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near · must-read
   - **Why it matters:** Predicts where a user will look next in egocentric video—anticipatory input for AR/VR interfaces.
2. [Learning Predictive Visuomotor Coordination](https://openaccess.thecvf.com/content/CVPR2026F/html/Jia_Learning_Predictive_Visuomotor_Coordination_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Jointly forecasts head pose, 3D gaze, and upper-body motion from egocentric input—intent modeling for robotics and AR, still research-stage.
3. [GazeOnce360: Fisheye-Based 360deg Multi-Person Gaze Estimation with Global-Local Feature Fusion](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_GazeOnce360_Fisheye-Based_360deg_Multi-Person_Gaze_Estimation_with_Global-Local_Feature_Fusion_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** near
   - **Why it matters:** Multi-person 3D gaze from one upward-facing fisheye camera—covers a tabletop room without per-person forward cameras.
4. [EgoXtreme: A Dataset for Robust Object Pose Estimation in Egocentric Views under Extreme Conditions](https://openaccess.thecvf.com/content/CVPR2026/html/Yoon_EgoXtreme_A_Dataset_for_Robust_Object_Pose_Estimation_in_Egocentric_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** A dataset for 6D object pose in egocentric views under extreme conditions—training fuel for smart-glasses context awareness, still research-stage.
5. [HUMAPS-4D: A Multimodal Dataset for HUman Motion Analysis with Physiological and Semantic informations](https://openaccess.thecvf.com/content/CVPR2026/html/Dabrowski_HUMAPS-4D_A_Multimodal_Dataset_for_HUman_Motion_Analysis_with_Physiological_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** A multimodal motion dataset adding physiological and semantic signals, aimed at human-motion analysis where video is privacy-restricted—research-stage.
6. [PAM: A Pose-Appearance-Motion Engine for Sim-to-Real HOI Video Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_PAM_A_Pose-Appearance-Motion_Engine_for_Sim-to-Real_HOI_Video_Generation_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** A pose-appearance-motion engine that unifies the fragmented hand-object-interaction generation tracks for sim-to-real HOI video—research-stage.

## 7. Industrial inspection, quality & anomaly detection

**Production scope:** Automating visual quality control and operational monitoring.

1. [Real-IAD MVN: A Multi-View Normal Vector Dataset and Benchmark for High-Fidelity Industrial Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2026F/html/Zhu_Real-IAD_MVN_A_Multi-View_Normal_Vector_Dataset_and_Benchmark_for_CVPRF_2026_paper.html)
   - **Grade:** A · **Novelty:** H · **Readiness:** near
   - **Why it matters:** A multi-view normal-vector dataset and benchmark targeting the subtle geometric defects that RGB anomaly detection misses.
2. [Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_Hierarchical_Point-Patch_Fusion_with_Adaptive_Patch_Codebook_for_3D_Shape_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near
   - **Why it matters:** 3D shape anomaly detection via point-patch fusion with an adaptive codebook—stronger geometric inspection.
3. [Towards Open-Vocabulary Industrial Defect Understanding with a Large-Scale Multimodal Dataset](https://openaccess.thecvf.com/content/CVPR2026/html/Ni_Towards_Open-Vocabulary_Industrial_Defect_Understanding_with_a_Large-Scale_Multimodal_Dataset_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** A 1M image-text defect dataset (60+ materials, 400+ defect types) so inspection can query defects outside a fixed catalog instead of training a new model per failure mode.
4. [Defect Cue-Preserved Structural Feature Refinement for Few-Shot Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Defect_Cue-Preserved_Structural_Feature_Refinement_for_Few-Shot_Anomaly_Detection_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** now
   - **Why it matters:** Few-shot anomaly detection that preserves defect cues across diverse sizes and shapes—usable where labeled defects are scarce.
5. [FastRef: Fast Prototype Refinement for Few-shot Industrial Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Li_FastRef_Fast_Prototype_Refinement_for_Few-shot_Industrial_Anomaly_Detection_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Fast prototype refinement that folds query-image statistics into few-shot anomaly detection—practical for data-scarce inspection lines.
6. [UniSpector: Towards Universal Open-set Defect Recognition via Spectral-Contrastive Visual Prompting](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_UniSpector_Towards_Universal_Open-set_Defect_Recognition_via_Spectral-Contrastive_Visual_Prompting_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Open-set defect recognition via spectral-contrastive visual prompting—detect unprecedented anomalies without retraining a closed-set model.

## 8. Medical, biological & scientific imaging

**Production scope:** Domain-specific perception where accuracy and evidence matter most.

1. [PBSBench: A Multi-Level Vision-Language Framework and Benchmark for Hematopathology Whole Slide Image Interpretation](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_PBSBench_A_Multi-Level_Vision-Language_Framework_and_Benchmark_for_Hematopathology_Whole_CVPRF_2026_paper.html)
   - **Grade:** A · **Novelty:** H · **Readiness:** near
   - **Why it matters:** A vision-language framework and benchmark for blood-smear whole-slide interpretation, focused on per-cell morphology—domain-specific diagnosis support, near-term.
2. [Rethinking Whole-Body CT Image Interpretation: An Abnormality-Centric Approach](https://openaccess.thecvf.com/content/CVPR2026F/html/Zhao_Rethinking_Whole-Body_CT_Image_Interpretation_An_Abnormality-Centric_Approach_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** research
   - **Why it matters:** A radiologist-built taxonomy and approach for localizing and describing abnormal CT findings across views—research-stage diagnosis support.
3. [LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_LUMINA_A_Multi-Vendor_Mammography_Benchmark_with_Energy_Harmonization_Protocol_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** A multi-vendor mammography benchmark that encodes acquisition energy and vendor metadata—addresses the domain shift that breaks deployed models.
4. [Focus on Background: Exploring SAM's Potential in Few-shot Medical Image Segmentation with Background-centric Prompting](https://openaccess.thecvf.com/content/CVPR2026/html/Bo_Focus_on_Background_Exploring_SAMs_Potential_in_Few-shot_Medical_Image_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Background-centric prompting that curbs SAM's over-segmentation on medical images in few-shot settings—research-stage.
5. [C3-Diff: Super-resolving Spatial Transcriptomics via Cross-modal Cross-content Contrastive Diffusion Modelling](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_C3-Diff_Super-resolving_Spatial_Transcriptomics_via_Cross-modal_Cross-content_Contrastive_Diffusion_Modelling_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Diffusion that super-resolves spatial transcriptomics by borrowing from paired imaging—scientific measurement, research-stage.
6. [Vision-Language Models for Automated 3D PET/CT Report Generation](https://openaccess.thecvf.com/content/CVPR2026F/html/Jiao_Vision-Language_Models_for_Automated_3D_PETCT_Report_Generation_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Vision-language automated reporting for 3D PET/CT to offload specialist workload—research-stage.

## 9. Geospatial, aerial & remote-sensing analytics

**Production scope:** Understanding the physical world from overhead and large-scale imagery.

1. [Semantic-Adaptive Diffusion for Dynamic Spatiotemporal Fusion](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Semantic-Adaptive_Diffusion_for_Dynamic_Spatiotemporal_Fusion_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Fuses satellite sources for higher spatio-temporal-resolution land monitoring—research-stage.
2. [UniGeoRS: A Unified Benchmark for Tri-view Geo-Localization](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_UniGeoRS_A_Unified_Benchmark_for_Tri-view_Geo-Localization_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near
   - **Why it matters:** A unified tri-view geo-localization benchmark spanning drone, ground, and satellite—addresses the data scarcity holding back cross-view models.
3. [SegEarth-R2: Towards Comprehensive Language-guided Segmentation for Remote Sensing Images](https://openaccess.thecvf.com/content/CVPR2026/html/Xin_SegEarth-R2_Towards_Comprehensive_Language-guided_Segmentation_for_Remote_Sensing_Images_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** Language-guided remote-sensing segmentation that handles complex, multi-granularity geospatial queries, not just single-target commands.
4. [ReAttnCLIP: Training-Free Open-Vocabulary Remote Sensing Image Segmentation via Re-defined Attention in CLIP](https://openaccess.thecvf.com/content/CVPR2026/html/Niu_ReAttnCLIP_Training-Free_Open-Vocabulary_Remote_Sensing_Image_Segmentation_via_Re-defined_Attention_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Training-free open-vocabulary remote-sensing segmentation by redefining CLIP attention—no fixed categories, no retraining.
5. [Prompt-driven Small Object Instance Segmentation in Earth Observation](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_Prompt-driven_Small_Object_Instance_Segmentation_in_Earth_Observation_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Prompted instance segmentation for the tiny objects in earth-observation imagery that detection-only methods miss.
6. [PAUL: Uncertainty-Guided Partition and Augmentation for Robust Cross-View Geo-Localization under Noisy Correspondence](https://openaccess.thecvf.com/content/CVPR2026/html/Li_PAUL_Uncertainty-Guided_Partition_and_Augmentation_for_Robust_Cross-View_Geo-Localization_under_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Robust cross-view geo-localization under noisy correspondence via uncertainty-guided partitioning—relevant to UAV navigation and aerial surveying.

## 10. Computational imaging & visual enhancement

**Production scope:** Improving what cameras capture before downstream perception or display.

1. [Efficient Real-Time Raw-to-Raw Denoising for Extreme Low-Light Ultra HD Video on Mobile Devices](https://openaccess.thecvf.com/content/CVPR2026/html/Pochimireddy_Efficient_Real-Time_Raw-to-Raw_Denoising_for_Extreme_Low-Light_Ultra_HD_Video_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** Real-time raw-to-raw denoising for 4K/8K video in sub-1-lux light on mobile—solves the latency that makes existing DNN restorers impractical at UHD.
2. [Evaluating Low-Light Image Enhancement Across Multiple Intensity Levels](https://openaccess.thecvf.com/content/CVPR2026F/html/Pilligua_Evaluating_Low-Light_Image_Enhancement_Across_Multiple_Intensity_Levels_CVPRF_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near
   - **Why it matters:** An evaluation showing single-condition training fails across light levels—pushes enhancement toward intensity-robust models.
3. [Towards Universal Computational Aberration Correction in Photographic Cameras: A Comprehensive Benchmark Analysis](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_Towards_Universal_Computational_Aberration_Correction_in_Photographic_Cameras_A_Comprehensive_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** near
   - **Why it matters:** A benchmark for lens-agnostic computational aberration correction, so correction generalizes instead of retraining per lens.
4. [Restore, Assess, Repeat: A Unified Framework for Iterative Image Restoration](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Restore_Assess_Repeat_A_Unified_Framework_for_Iterative_Image_Restoration_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** An iterative restoration framework that assesses its own output and re-restores—better generalization to unknown, composite degradations.
5. [CARD: Correlation Aware Restoration with Diffusion](https://openaccess.thecvf.com/content/CVPR2026/html/Nezakati_CARD_Correlation_Aware_Restoration_with_Diffusion_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Diffusion restoration that models spatially correlated sensor noise instead of i.i.d. Gaussian—closer to real camera readout.
6. [CtrlISP: Rescuing Low-Light RAW Images via Controllable Neural ISP](https://openaccess.thecvf.com/content/CVPR2026F/html/Zhang_CtrlISP_Rescuing_Low-Light_RAW_Images_via_Controllable_Neural_ISP_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** near
   - **Why it matters:** A controllable neural ISP that rescues extremely dark low-light RAW where conventional ISPs produce noise and color casts.

## 11. Visual search, multimodal understanding & agents

**Production scope:** Natural-language access to images, video, documents, and visual tasks.

1. [SenseSearch: Empowering Vision-Language Models with High-Resolution Agentic Search-Reasoning via Reinforcement Learning](https://openaccess.thecvf.com/content/CVPR2026/html/Chng_SenseSearch_Empowering_Vision-Language_Models_with_High-Resolution_Agentic_Search-Reasoning_via_Reinforcement_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** RL-trained agentic search-reasoning that lets a VLM zoom and search high-resolution images—fine-grained, knowledge-intensive visual QA.
2. [MM-SeR: Multimodal Self-Refinement for Lightweight Image Captioning](https://openaccess.thecvf.com/content/CVPR2026/html/Song_MM-SeR_Multimodal_Self-Refinement_for_Lightweight_Image_Captioning_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** L · **Readiness:** now
   - **Why it matters:** A lightweight self-refining captioner for streaming use—captioning for chatbots and robots without a heavy MLLM's cost.
3. [Thinking with Video: Video Generation as a Promising Multimodal Reasoning Paradigm](https://openaccess.thecvf.com/content/CVPR2026/html/Tong_Thinking_with_Video_Video_Generation_as_a_Promising_Multimodal_Reasoning_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Recasts reasoning as video generation so the model reasons over continuous processes, not the frozen frames image reasoning is stuck with—promising but early.
4. [SuperGlasses: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses](https://openaccess.thecvf.com/content/CVPR2026F/html/Jiang_SuperGlasses_Benchmarking_Vision_Language_Models_as_Intelligent_Agents_for_AI_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** H · **Readiness:** now
   - **Why it matters:** A benchmark for VLMs as smart-glasses agents doing knowledge-grounded VQA—reveals where current models fall short on wearables.
5. [Draft and Refine with Visual Experts](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Draft_and_Refine_with_Visual_Experts_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** near
   - **Why it matters:** Quantifies and reduces LVLM reliance on language priors using visual experts—less hallucination, better grounding.
6. [ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning](https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ARM-Thinker_Reinforcing_Multimodal_Generative_Reward_Models_with_Agentic_Tool_Use_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** An agentic multimodal reward model that uses tools to verify—reducing reward-model hallucination when aligning vision-language systems—research-stage.

## 12. Generative visual media & content production

**Production scope:** Creating and editing visual content for media, design, and simulation.

1. [Towards Storytelling Animations: Joint Synthesis of Human and Camera Motions](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Towards_Storytelling_Animations_Joint_Synthesis_of_Human_and_Camera_Motions_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Joint synthesis of character and camera motion for 3D animation—research-stage content tooling.
2. [AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_AvatarPointillist_AutoRegressive_4D_Gaussian_Avatarization_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Autoregressive 4D Gaussian avatars from a single portrait—research-stage avatar generation.
3. [Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Learning_to_Generate_Highly_Dynamic_Videos_using_Synthetic_Motion_Data_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Generates fast, controllable motion by addressing the scarcity of dynamic examples with synthetic motion data—research-stage.
4. [LottieGPT: Tokenizing Vector Animation for Autoregressive Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_LottieGPT_Tokenizing_Vector_Animation_for_Autoregressive_Generation_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Tokenizes vector animation for autoregressive generation—editable, resolution-independent output current video models can't produce—research-stage.
5. [First Frame Is the Place to Go for Video Content Customization](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_First_Frame_Is_the_Place_to_Go_for_Video_Content_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Reuses the first frame as the control handle for video customization—research-stage editing technique.
6. [Human Geometry Distribution for 3D Animation Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_Human_Geometry_Distribution_for_3D_Animation_Generation_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** Generates clothed-human geometry animation with fine detail from limited data—usable now for 3D animation assets.

## 13. Data engines, adaptation & continuous learning

**Production scope:** The machinery that turns deployed data into improving models.

1. [Dynamic Pseudo-Label Assignment and Consistent Prototypical Learning for Few-Shot Class-Incremental Learning](https://openaccess.thecvf.com/content/CVPR2026F/html/Mao_Dynamic_Pseudo-Label_Assignment_and_Consistent_Prototypical_Learning_for_Few-Shot_Class-Incremental_CVPRF_2026_paper.html)
   - **Grade:** A · **Novelty:** L · **Readiness:** now · must-read
   - **Why it matters:** Few-shot class-incremental learning that avoids pseudo-label collapse—add classes from a few samples without forgetting.
2. [Mind the Gap: Transferring Labels to Align Object Detection Datasets](https://openaccess.thecvf.com/content/CVPR2026/html/Kennerley_Mind_the_Gap_Transferring_Labels_to_Align_Object_Detection_Datasets_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near
   - **Why it matters:** Transfers labels to merge object-detection datasets with mismatched taxonomies and boxes, no manual relabeling—directly useful for data pipelines.
3. [Portable Active Learning for Object Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Sharma_Portable_Active_Learning_for_Object_Detection_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** L · **Readiness:** now
   - **Why it matters:** Cuts detection annotation cost by selecting the most informative boxes to label—practical labeling efficiency.
4. [HyCal: A Training-Free Prototype Calibration Method for Cross-Discipline Few-Shot Class-Incremental Learning](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_HyCal_A_Training-Free_Prototype_Calibration_Method_for_Cross-Discipline_Few-Shot_Class-Incremental_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** L · **Readiness:** now
   - **Why it matters:** Training-free prototype calibration for cross-discipline few-shot incremental learning, where domains and class balance differ.
5. [Conformal Cross-Modal Active Learning](https://openaccess.thecvf.com/content/CVPR2026F/html/Nguyen_Conformal_Cross-Modal_Active_Learning_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Active learning over foundation-model features with conformal guarantees—data-efficient labeling you can put a bound on.
6. [Bootstrap Your Own Classifier: Your Pretrained Vision Models are Secretly Strong Continual Learners](https://openaccess.thecvf.com/content/CVPR2026F/html/Gong_Bootstrap_Your_Own_Classifier_Your_Pretrained_Vision_Models_are_Secretly_CVPRF_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Fixes the backbone/classifier initialization mismatch so pretrained vision models become strong continual learners.

## 14. Efficient, robust & trustworthy deployment

**Production scope:** Cross-cutting work required to operate vision systems in production.

1. [Verifying Neural Network Robustness with Dual Perturbations](https://openaccess.thecvf.com/content/CVPR2026/html/Duong_Verifying_Neural_Network_Robustness_with_Dual_Perturbations_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** near
   - **Why it matters:** Formally verifies robustness against combined correlated-distortion and pixel noise together, not separately—for safety-critical systems.
2. [CamPI: Physical Adversarial Examples through Camera Power Signal Injection](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_CamPI_Physical_Adversarial_Examples_through_Camera_Power_Signal_Injection_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** An invisible physical adversarial attack via camera power-signal injection—exposes a deployment threat surface; defensive research signal.
3. [A Combination of Noise and Bilateral Filters Achieve Supralinear and Scalable Adversarial Robustness in CNNs](https://openaccess.thecvf.com/content/CVPR2026/html/Stalder_A_Combination_of_Noise_and_Bilateral_Filters_Achieve_Supralinear_and_CVPR_2026_paper.html)
   - **Grade:** A · **Novelty:** M · **Readiness:** now · must-read
   - **Why it matters:** Achieves scalable adversarial robustness without expensive, attack-specific adversarial training.
4. [AntiStyler: Defending Object Detection Models Against Adversarial Patch Attacks Using Style Removal](https://openaccess.thecvf.com/content/CVPR2026/html/Yankelev_AntiStyler_Defending_Object_Detection_Models_Against_Adversarial_Patch_Attacks_Using_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** now
   - **Why it matters:** Defends detectors against adversarial patches via style removal, without the benign-accuracy loss or latency of prior defenses—usable in real-time security.
5. [Evidential Neural Radiance Fields](https://openaccess.thecvf.com/content/CVPR2026/html/Duan_Evidential_Neural_Radiance_Fields_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Adds uncertainty estimation to NeRF for safety-critical deployment—research-stage trust tooling.
6. [PRIMU: Uncertainty Estimation for Novel Views in Gaussian Splatting from Primitive-Based Representations of Error and Coverage](https://openaccess.thecvf.com/content/CVPR2026/html/Gottwald_PRIMU_Uncertainty_Estimation_for_Novel_Views_in_Gaussian_Splatting_from_CVPR_2026_paper.html)
   - **Grade:** B · **Novelty:** M · **Readiness:** research
   - **Why it matters:** Post-hoc uncertainty estimation for Gaussian-Splatting novel views—reliability for robotics and medicine, research-stage.
