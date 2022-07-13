# Few Shot Object Detection Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

*NOTE:* If your paper is not in the list, please feel free to [raise an issue](https://github.com/gaobb/Few-Shot-Object-Detection-Papers/issues) or drop me an [e-mail](mailto:csgaobb@gmail.com?subject=[GitHub]%fewshot%papers).

## Survey
| Methods | Venue |  Project|
| :-----|:-----:|:-----:|
|[Few-Shot Object Detection: A Survey](https://arxiv.org/pdf/2112.11699.pdf)|arXiv'21|-|
|[A Comparative Review of Recent Few-Shot Object Detection Algorithms](https://arxiv.org/pdf/2111.00201.pdf)|arXiv'21|-|
|[Few-Shot Object Detection: A Survey](https://dl.acm.org/doi/pdf/10.1145/3519022)|TNNLS'22|-|
|[A Survey of Self-Supervised and Few-Shot Object Detection](https://arxiv.org/pdf/2110.14711.pdf)|arXiv'21| [project](https://gabrielhuang.github.io/fsod-survey/)|


## 2022
| Methods | Venue | CODE | Type| Detector | COCO 1/5/10/30-shot AP |
| :-----|:-----:|:---:|:----:|:-----|:-----:|
|[DETReg](https://arxiv.org/pdf/2106.04550.pdf) |CVPR|[CODE](https://github.com/amirbar/DETReg)| Fine-tuning| Deformable DETR |-/-/-/-| 
|[Label, Verify, Correct](https://openaccess.thecvf.com/content/CVPR2022/papers/Kaul_Label_Verify_Correct_A_Simple_Few_Shot_Object_Detection_Method_CVPR_2022_paper.pdf)| CVPR | [CODE](https://github.com/prannaykaul/lvc)|Pseudo-Label Fine-tuning|  Faster R-CNN R-101+DINO ViT-S| -/-/17.8/24.5|
|[Sylph](https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_Sylph_A_Hypernetwork_Framework_for_Incremental_Few-Shot_Object_Detection_CVPR_2022_paper.pdf)| CVPR |-| Meta-learning|Faster R-CNN R-50|-/-/-/-|
|[FCT](https://openaccess.thecvf.com/content/CVPR2022/papers/Han_Few-Shot_Object_Detection_With_Fully_Cross-Transformer_CVPR_2022_paper.pdf)| CVPR | - |Meta-learning| Faster R-CNN-PVTv2-B2-Li|5.6/14.0/17.1/21.4|
|[KFSOD](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_Kernelized_Few-Shot_Object_Detection_With_Efficient_Integral_Aggregation_CVPR_2022_paper.pdf)| CVPR |[CODE](https://github.com/ZS123-lang/KFSOD) |Meta-learning| Faster-RCN  R-50|-/-/18.5/-|


## 2021
| Methods | Venue | CODE |Type| Detector | COCO 1/5/10/30-shot AP |
| :-----|:-----:|:----:|:----:|:-----|:-----:|
|[DeFRCN](https://openaccess.thecvf.com/content/ICCV2021/papers/Qiao_DeFRCN_Decoupled_Faster_R-CNN_for_Few-Shot_Object_Detection_ICCV_2021_paper.pdf) | ICCV | [CODE](https://github.com/er-muyue/DeFRCN)|Fine-tuning|Faster R-CNN R-101| 7.7/15.9/18.5/22.6|
|[FSOD$^{up}$](https://arxiv.org/abs/2103.01077)| ICCV |[CODE](https://github.com/AmingWu/UP-FSOD)|Fine-tuning|Faster R-CNN R-101| -/-/11.0/15.6|
|[DAnA](https://arxiv.org/pdf/2102.12152.pdf)|TMM|[CODE](https://github.com/Tung-I/Dual-awareness-Attention-for-Few-shot-Object-Detection)|Meta-learning|Faster R-CNN R-50| -/-/18.6/21.6|
|[FADI](https://proceedings.neurips.cc/paper/2021/file/8a1e808b55fde9455cb3d8857ed88389-Paper.pdf)| NeurIPS | [CODE](https://github.com/yhcao6/FADI)|Fine-tuning|Faster R-CNN R-101| 5.7/-/12.2/16.1|
|[SRR-FSD](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhu_Semantic_Relation_Reasoning_for_Shot-Stable_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|-|Fine-tuning|Faster R-CNN R-101| -/-/11.3/14.7|
|[IMTFA](https://openaccess.thecvf.com/content/CVPR2021/papers/Ganea_Incremental_Few-Shot_Instance_Segmentation_CVPR_2021_paper.pdf)| CVPR |[CODE](https://github.com/danganea/iMTFA)|Fine-tuning|Faster R-CNN R-50| 2.4/6.6/8.5/-|
|[CME](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Beyond_Max-Margin_Class_Margin_Equilibrium_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|[CODE](https://github.com/Bohao-Lee/CME)|Meta-learning|Meta YOLO|-/-/15.1/16.9|
|[DCNet](https://openaccess.thecvf.com/content/CVPR2021/papers/Hu_Dense_Relation_Distillation_With_Context-Aware_Aggregation_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|[CODE](https://github.com/hzhupku/DCNet)|Meta-learning|Faster R-CNN R-101| -/-/12.8/18.6|
|[TIP](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Transformation_Invariant_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|-|Meta-learning|Faster R-CNN R-101|-/-/16.3/18.3|
|[FSCE](https://openaccess.thecvf.com/content/CVPR2021/papers/Sun_FSCE_Few-Shot_Object_Detection_via_Contrastive_Proposal_Encoding_CVPR_2021_paper.pdf)|CVPR|[CODE](https://github.com/MegviiDetection/FSCE)|Fine-tuning|Faster R-CNN R-101|-/-/11.1/15.3|
|[Retentive R-CNN](https://openaccess.thecvf.com/content/CVPR2021/papers/Fan_Generalized_Few-Shot_Object_Detection_Without_Forgetting_CVPR_2021_paper.pdf)|CVPR|[CODE](https://github.com/Megvii-BaseDetection/GFSD)|Fine-tuning|R-CNN-ResNet-101|-/8.3/10.5/13.8|
|[Halluc](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhang_Hallucination_Improves_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|[CODE](https://github.com/pppplin/HallucFsDet)|Fine-tuning|Faster R-CNN R-101|4.4/-/-/-|
|[StarNet](http://arxiv.org/abs/2003.06798)|AAAI|[CODE](-)|Meta-learning| ResNet-12 |-/-/-/-|

## 2020
| Title | Venue | CODE |Type|Detector | COCO 1/5/10/30-shot AP |
| :-----|:-----:|:----:|:----:|:-----|:-----:|
|[Context-Transformer](https://arxiv.org/pdf/2003.07304.pdf)| AAAI |[CODE](https://github.com/Ze-Yang/Context-Transformer)|Fine-tuning| SSD | -/-/-/-/|
|[FSOD-ARPN-MRD](https://arxiv.org/abs/1908.01998)|CVPR |[CODE](https://github.com/fanq15/Few-Shot-Object-Detection-Dataset)|Meta-Learning| Faster R-CNN R-50| -/-/-/-/|
|[ONCE](https://openaccess.thecvf.com/content_CVPR_2020/papers/Perez-Rua_Incremental_Few-Shot_Object_Detection_CVPR_2020_paper.pdf)|CVPR| -|Meta-learning| CentreNet | -/-/-/-/|
|[TFA](https://arxiv.org/abs/2003.06957)| ICML|[CODE](https://github.com/ucbdrive/few-shot-object-detection)|Fine-tuning| Faster R-CNN R-101 |-/-/10.0/13.7|
|[FSDetView](https://arxiv.org/abs/2007.12107)|ECCV|[CODE](http://imagine.enpc.fr/~xiaoy/FSDetView/)|Meta-learning| Faster R-CNN R-101 |-/-/12.5/14.7|
|[MPSR](https://arxiv.org/pdf/2007.09384.pdf)| ECCV |[CODE](https://github.com/jiaxi-wu/MPSR)|Fine-tuning|Faster R-CNN R-101|-/-/9.8/14.1|
|[NP-RepMet](https://arxiv.org/pdf/2010.11714.pdf)|NeurIPS|[CODE](https://github.com/yang-yk/NP-RepMet)| Fine-tuning|Faster R-CNN R-101+DCN | -/-/-/-|
[Meta-RCNN](https://dl.acm.org/doi/10.1145/3394171.3413832)| ACM-MM |- |Meta-learning| Faster R-CNN R-101 |-/-/8.7/12.4|


## References
[DETReg: Unsupervised Pretraining with Region Priors for Object Detection](https://arxiv.org/pdf/2106.04550.pdf),CVPR 2022.
[Label, Verify, Correct: A Simple Few Shot Object Detection Method](https://openaccess.thecvf.com/content/CVPR2022/papers/Kaul_Label_Verify_Correct_A_Simple_Few_Shot_Object_Detection_Method_CVPR_2022_paper.pdf), CVPR 2022.
[Sylph: A Hypernetwork Framework for Incremental Few-shot Object Detection](https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_Sylph_A_Hypernetwork_Framework_for_Incremental_Few-Shot_Object_Detection_CVPR_2022_paper.pdf), CVPR 2022.
[FCT: Few-Shot Object Detection with Fully Cross-Transformer](https://openaccess.thecvf.com/content/CVPR2022/papers/Han_Few-Shot_Object_Detection_With_Fully_Cross-Transformer_CVPR_2022_paper.pdf),CVPR 2022.
[KFSOD: Kernelized Few-shot Object Detection with Efficient Integral Aggregation](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_Kernelized_Few-Shot_Object_Detection_With_Efficient_Integral_Aggregation_CVPR_2022_paper.pdf), CVPR 2022.
[DeFRCN: Decoupled Faster R-CNN for Few-Shot Object Detection](https://openaccess.thecvf.com/content/ICCV2021/papers/Qiao_DeFRCN_Decoupled_Faster_R-CNN_for_Few-Shot_Object_Detection_ICCV_2021_paper.pdf), ICCV 2021.
[FSOD$^{up}$: Universal-Prototype Augmentation for Few-Shot Object Detection](https://arxiv.org/abs/2103.01077), ICCV 2021.
[DAnA: Dual-awareness Attention for Few-Shot Object Detection](https://arxiv.org/pdf/2102.12152.pdf), TMM 2021.
[FADI: Few-Shot Object Detection via Association and Discrimination](https://proceedings.neurips.cc/paper/2021/file/8a1e808b55fde9455cb3d8857ed88389-Paper.pdf)| NeurIPS |
[SRR-FSD: Semantic Relation Reasoning for Shot-Stable Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhu_Semantic_Relation_Reasoning_for_Shot-Stable_Few-Shot_Object_Detection_CVPR_2021_paper.pdf), CVPR 2021.
[IMTFA: Incremental Few-Shot Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2021/papers/Ganea_Incremental_Few-Shot_Instance_Segmentation_CVPR_2021_paper.pdf), CVPR 2021.
[CME: Beyond Max-Margin, Class Margin Equilibrium for Few-shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Beyond_Max-Margin_Class_Margin_Equilibrium_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf), CVPR 2021.
[DCNet: Dense Relation Distillation with Context-aware Aggregation for Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Hu_Dense_Relation_Distillation_With_Context-Aware_Aggregation_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)
[TIP: Transformation Invariant Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Transformation_Invariant_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)
[FSCE: Few-Shot Object Detection via Contrastive Proposal Encoding](https://openaccess.thecvf.com/content/CVPR2021/papers/Sun_FSCE_Few-Shot_Object_Detection_via_Contrastive_Proposal_Encoding_CVPR_2021_paper.pdf), CVPR 2021.
[Retentive R-CNN: Generalized Few-Shot Object Detection without Forgetting](https://openaccess.thecvf.com/content/CVPR2021/papers/Fan_Generalized_Few-Shot_Object_Detection_Without_Forgetting_CVPR_2021_paper.pdf), CVPR 2021.
[Halluc: Hallucination Improves Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhang_Hallucination_Improves_Few-Shot_Object_Detection_CVPR_2021_paper.pdf), CVPR 2021.
[StarNet: towards Weakly Supervised Few-Shot Object Detection](http://arxiv.org/abs/2003.06798), AAAI 2021.
[Context-Transformer: Tackling Object Confusion for Few-Shot Detection](https://arxiv.org/pdf/2003.07304.pdf),AAAI 2020.
[FSOD-ARPN-MRD: Few-Shot Object Detection With Attention-RPN and Multi-Relation Detector](https://arxiv.org/abs/1908.01998), CVPR 2020.
[ONCE: Incremental Few-Shot Object Detection](https://openaccess.thecvf.com/content_CVPR_2020/papers/Perez-Rua_Incremental_Few-Shot_Object_Detection_CVPR_2020_paper.pdf), CVPR 2020.
[TFA: Frustratingly Simple Few-Shot Object Detection](https://arxiv.org/abs/2003.06957), ICML 2020.
[FSDetView: Few-Shot Object Detection and Viewpoint Estimation for Objects in the Wild](https://arxiv.org/abs/2007.12107), ECCV 2020.
[MPSR: Multi-Scale Positive Sample Refinement for Few-Shot Object Detection](https://arxiv.org/pdf/2007.09384.pdf), ECCV 2020.
[NP-RepMet: Restoring Negative Information in Few-Shot Object Detection](https://arxiv.org/pdf/2010.11714.pdf), NeurIPS 2020.
[Meta-RCNN: Meta Learning for Few-Shot Object Detection](https://dl.acm.org/doi/10.1145/3394171.3413832), ACM-MM 2020.