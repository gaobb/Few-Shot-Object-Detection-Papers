# Few Shot Object Detection Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

*NOTE:* If your paper is not in the list, please feel free to [raise an issue](https://github.com/gaobb/Few-Shot-Object-Detection-Papers/issues) or drop me an [e-mail](mailto:csgaobb@gmail.com?subject=[GitHub]%fewshot%papers).

## Survey
| Methods | Venue |  Project|
| :-----|:-----:|:-----:|
|[Few-Shot Object Detection: A Survey](https://arxiv.org/pdf/2112.11699.pdf)|arXiv'21|-|
|[A Comparative Review of Recent Few-Shot Object Detection Algorithms](https://arxiv.org/pdf/2111.00201.pdf)|arXiv'21|-|
|[Few-Shot Object Detection: A Survey](https://dl.acm.org/doi/pdf/10.1145/3519022)|TNNLS'22|-|
|[A Survey of Self-Supervised and Few-Shot Object Detection](https://arxiv.org/pdf/2110.14711.pdf)|arXiv'21| [project](https://gabrielhuang.github.io/fsod-survey/)|



| Method | Venue | Year| Backbone|Detector|Type| COCO 1/5/10/30-shot AP |Code|
| :-----|:-----:|:-----:|:---:|:---:|:----:|:-----|:-----:|
[DCFS](https://openreview.net/pdf?id=dVXO3Orjmxk)| NeurIPS | 2022| R-101| Faster-RCNN |Fine-tuning| 8.1/12.1/14.4/16.6/19.5/22.7 |[PyTorch](https://csgaobb.github.io/Projects/DCFS)|
[FewX](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136790707.pdf)|ECCV|2022| R-50 |Faster R-CNN|Fine-tuning|-/15.1/-/-|[PyTorch](https://github.com/fanq15/FewX)|
[MFDC](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690569.pdf)|ECCV|2022| R-101 |Faster R-CNN|Fine-tuning|10.8/13.9/15.0/16.4/19.4/22.7|[PyTorch](https://github.com/WuShuang1998/MFDC)|
[AcroFOD](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136930661.pdf)|ECCV|2022|-|YOLOv5|Fine-tuning|-/-/-/- |[PyTorch](https://github.com/Hlings/AcroFOD)|
[TENET](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800300.pdf)|ECCV|2022|R-50|-|Fine-tuning|-/-/19.1/- |[PyTorch](https://github.com/ZS123-lang/TENET)|
|[MoFSOD](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800354.pdf)|ECCV|2022|R-50|Faster RCNN,Cascade R-CNN,CenterNet2,RetinaNet,Deformable-DETR|Fine-tuning|-/-/-/- |[-](https://github.com/amazon-research/few-shot-object-detection-benchmark)|
|[MRSN](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800388.pdf)|ECCV|2022|R-101|Faster R-CNN|Fine-tuning|-/-/15.7/17.5 |[-](https://github.com/MMatx/MRSN)|
|[KD-DeFRCN](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136700279.pdf)|ECCV|2022|R-101|Faster R-CNN|Fine-tuning|-/-/18.9/22.6 |-|
|[DETReg](https://arxiv.org/pdf/2106.04550.pdf) |CVPR|2022|DETReg|Deformable DETR|Fine-tuning|-/-/~~25.0~~/~~30.0~~| [PyTorch](https://github.com/amirbar/DETReg)|
|[Label, Verify, Correct](https://openaccess.thecvf.com/content/CVPR2022/papers/Kaul_Label_Verify_Correct_A_Simple_Few_Shot_Object_Detection_Method_CVPR_2022_paper.pdf)| CVPR |2022|R-101+DINO ViT-S|Faster R-CNN|Fine-tuning| -/-/17.8/24.5|[PyTorch](https://github.com/prannaykaul/lvc)|
|[Sylph](https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_Sylph_A_Hypernetwork_Framework_for_Incremental_Few-Shot_Object_Detection_CVPR_2022_paper.pdf)| CVPR |2022|R-50|Faster R-CNN| Meta-learning|-/-/-/-|-|
|[FCT](https://openaccess.thecvf.com/content/CVPR2022/papers/Han_Few-Shot_Object_Detection_With_Fully_Cross-Transformer_CVPR_2022_paper.pdf)| CVPR |2022|PVTv2-B2-Li| Faster R-CNN |Meta-learning|5.6/14.0/17.1/21.4|-|
|[KFSOD](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_Kernelized_Few-Shot_Object_Detection_With_Efficient_Integral_Aggregation_CVPR_2022_paper.pdf)| CVPR |2022|R-50|Faster-RCN|Meta-learning|-/-/18.5/-|[-](https://github.com/ZS123-lang/KFSOD)|
|[DeFRCN](https://openaccess.thecvf.com/content/ICCV2021/papers/Qiao_DeFRCN_Decoupled_Faster_R-CNN_for_Few-Shot_Object_Detection_ICCV_2021_paper.pdf) | ICCV | 2021|R-101|Faster R-CNN| Fine-tuning|7.7/15.9/18.5/22.6|[PyTorch](https://github.com/er-muyue/DeFRCN)
|[FSOD$^{up}$](https://arxiv.org/abs/2103.01077)| ICCV |2021|R-101|Faster R-CNN|Fine-tuning|-/-/11.0/15.6|[PyTorch](https://github.com/AmingWu/UP-FSOD)
|[DAnA](https://arxiv.org/pdf/2102.12152.pdf)|TMM|2021|R-50|Faster R-CNN|Meta-learning|-/-/18.6/21.6|[PyTorch](https://github.com/Tung-I/Dual-awareness-Attention-for-Few-shot-Object-Detection)|
|[FADI](https://proceedings.neurips.cc/paper/2021/file/8a1e808b55fde9455cb3d8857ed88389-Paper.pdf)| NeurIPS |2021|R-101|Faster R-CNN|Fine-tuning| 5.7/-/12.2/16.1|[PyTorch](https://github.com/yhcao6/FADI)|
|[SRR-FSD](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhu_Semantic_Relation_Reasoning_for_Shot-Stable_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|2021|R-101|Faster R-CNN|Fine-tuning| -/-/11.3/14.7|-|
|[IMTFA](https://openaccess.thecvf.com/content/CVPR2021/papers/Ganea_Incremental_Few-Shot_Instance_Segmentation_CVPR_2021_paper.pdf)| CVPR |2021|R-50|Faster R-CNN|Fine-tuning| 2.4/6.6/8.5/-|[PyTorch](https://github.com/danganea/iMTFA)|
|[CME](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Beyond_Max-Margin_Class_Margin_Equilibrium_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|2021|YOLO|Meta YOLO|Meta-learning|-/-/15.1/16.9|[PyTorch](https://github.com/Bohao-Lee/CME)|
|[DCNet](https://openaccess.thecvf.com/content/CVPR2021/papers/Hu_Dense_Relation_Distillation_With_Context-Aware_Aggregation_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|2021|R-101|Faster R-CNN|Meta-learning| -/-/12.8/18.6|[](https://github.com/hzhupku/DCNet)|
|[TIP](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Transformation_Invariant_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|2021|R-101|Faster R-CNN|Meta-learning|-/-/16.3/18.3|-|
|[FSCE](https://openaccess.thecvf.com/content/CVPR2021/papers/Sun_FSCE_Few-Shot_Object_Detection_via_Contrastive_Proposal_Encoding_CVPR_2021_paper.pdf)|CVPR|2021|R-101|Faster R-CNN |Fine-tuning|-/-/11.1/15.3|[PyTorch](https://github.com/MegviiDetection/FSCE)|
|[Retentive R-CNN](https://openaccess.thecvf.com/content/CVPR2021/papers/Fan_Generalized_Few-Shot_Object_Detection_Without_Forgetting_CVPR_2021_paper.pdf)|CVPR|2021|R-101|R-CNN|Fine-tuning|-/8.3/10.5/13.8|[PyTorch](https://github.com/Megvii-BaseDetection/GFSD)|
|[Halluc](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhang_Hallucination_Improves_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)|CVPR|2021|R-101|Faster R-CNN|Fine-tuning|4.4/-/-/-|[-](https://github.com/pppplin/HallucFsDet)
|[StarNet](http://arxiv.org/abs/2003.06798)|AAAI|2021|ResNet-12|Meta-learning| ResNet-12 |-/-/-/-|-|
|[Context-Transformer](https://arxiv.org/pdf/2003.07304.pdf)| AAAI |2020||SSD|Fine-tuning| -/-/-/-/|[PyTorch](https://github.com/Ze-Yang/Context-Transformer)
|[FSOD-ARPN-MRD](https://arxiv.org/abs/1908.01998)|CVPR |2020|R-50|Faster R-CNN|Meta-Learning| -/-/-/-/|[-](https://github.com/fanq15/Few-Shot-Object-Detection-Dataset)|
|[ONCE](https://openaccess.thecvf.com/content_CVPR_2020/papers/Perez-Rua_Incremental_Few-Shot_Object_Detection_CVPR_2020_paper.pdf)|CVPR|2020||CentreNet|Meta-learning | -/-/-/-/|-|
|[TFA](https://arxiv.org/abs/2003.06957)| ICML|2020|R-101|Faster R-CNN|Fine-tuning|-/-/10.0/13.7|[PyTorch](https://github.com/ucbdrive/few-shot-object-detection)|
|[FSDetView](https://arxiv.org/abs/2007.12107)|ECCV|2020|R-101|Faster R-CNN |Meta-learning|-/-/12.5/14.7|[PyTorch](http://imagine.enpc.fr/~xiaoy/FSDetView/)
|[MPSR](https://arxiv.org/pdf/2007.09384.pdf)| ECCV |2020|R-101|Faster R-CNN| Fine-tuning|-/-/9.8/14.1|[PyTorch](https://github.com/jiaxi-wu/MPSR)|
|[NP-RepMet](https://arxiv.org/pdf/2010.11714.pdf)|NeurIPS|2020|R-101| Faster R-CNN + DCN|Fine-tuning| -/-/-/-|[MXNet](https://github.com/yang-yk/NP-RepMet)|
[Meta-RCNN](https://dl.acm.org/doi/10.1145/3394171.3413832)| ACM-MM |2020|R-101|Faster R-CNN |Meta-learning |-/-/8.7/12.4|-|


## References
- [DCFS: Decoupling Classifier for Boosting Few-shot Object Detection and Instance Segmentation](https://openreview.net/pdf?id=dVXO3Orjmxk), NeurIPS 2022.
- [FewX: Few-Shot Object Detection with Model Calibration](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136790707.pdf), ECCV 2022.
- [MFDC: Multi-Faceted Distillation of Base-Novel Commonality for Few-shot Object Detection](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690569.pdf),ECCV 2022. 
- [AcroFOD: An Adaptive Method for Cross-domain Few-shot Object Detection](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136930661.pdf), ECCV 2022.
- [TENET: Time-rEversed diffusioN tEnsor Transformer: A new TENET of Few-Shot Object Detection](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800300.pdf)], ECCV 2022.
- [MoFSOD: Rethinking Few-Shot Object Detection on A Multi-Domain Benchmark](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800354.pdf), ECCV 2022.
- [MRSN: Mutually Reinforcing Structure with Proposal Contrastive Consistency for Few-Shot Object Detection](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800388.pdf), ECCV 2022.
- [KD-DeFRCN: Few-Shot Object Detection by Knowledge Distillation Using Bag-of-Visual-Words Representations](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136700279.pdf), ECCV 2022.
- [DETReg: Unsupervised Pretraining with Region Priors for Object Detection](https://arxiv.org/pdf/2106.04550.pdf),CVPR 2022.
- [Label, Verify, Correct: A Simple Few Shot Object Detection Method](https://openaccess.thecvf.com/content/CVPR2022/papers/Kaul_Label_Verify_Correct_A_Simple_Few_Shot_Object_Detection_Method_CVPR_2022_paper.pdf), CVPR 2022.
- [Sylph: A Hypernetwork Framework for Incremental Few-shot Object Detection](https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_Sylph_A_Hypernetwork_Framework_for_Incremental_Few-Shot_Object_Detection_CVPR_2022_paper.pdf), CVPR 2022.
- [FCT: Few-Shot Object Detection with Fully Cross-Transformer](https://openaccess.thecvf.com/content/CVPR2022/papers/Han_Few-Shot_Object_Detection_With_Fully_Cross-Transformer_CVPR_2022_paper.pdf),CVPR 2022.
- [KFSOD: Kernelized Few-shot Object Detection with Efficient Integral Aggregation](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_Kernelized_Few-Shot_Object_Detection_With_Efficient_Integral_Aggregation_CVPR_2022_paper.pdf), CVPR 2022.
- [DeFRCN: Decoupled Faster R-CNN for Few-Shot Object Detection](https://openaccess.thecvf.com/content/ICCV2021/papers/Qiao_DeFRCN_Decoupled_Faster_R-CNN_for_Few-Shot_Object_Detection_ICCV_2021_paper.pdf), ICCV 2021.
- [FSOD$^{up}$: Universal-Prototype Augmentation for Few-Shot Object Detection](https://arxiv.org/abs/2103.01077), ICCV 2021.
- [DAnA: Dual-awareness Attention for Few-Shot Object Detection](https://arxiv.org/pdf/2102.12152.pdf), TMM 2021.
- [FADI: Few-Shot Object Detection via Association and Discrimination](https://proceedings.neurips.cc/paper/2021/file/8a1e808b55fde9455cb3d8857ed88389-Paper.pdf),NeurIPS, 2021.
- [SRR-FSD: Semantic Relation Reasoning for Shot-Stable Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhu_Semantic_Relation_Reasoning_for_Shot-Stable_Few-Shot_Object_Detection_CVPR_2021_paper.pdf), CVPR 2021.
- [IMTFA: Incremental Few-Shot Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2021/papers/Ganea_Incremental_Few-Shot_Instance_Segmentation_CVPR_2021_paper.pdf), CVPR 2021.
- [CME: Beyond Max-Margin, Class Margin Equilibrium for Few-shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Beyond_Max-Margin_Class_Margin_Equilibrium_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf), CVPR 2021.
- [DCNet: Dense Relation Distillation with Context-aware Aggregation for Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Hu_Dense_Relation_Distillation_With_Context-Aware_Aggregation_for_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)
- [TIP: Transformation Invariant Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Transformation_Invariant_Few-Shot_Object_Detection_CVPR_2021_paper.pdf)
- [FSCE: Few-Shot Object Detection via Contrastive Proposal Encoding](https://openaccess.thecvf.com/content/CVPR2021/papers/Sun_FSCE_Few-Shot_Object_Detection_via_Contrastive_Proposal_Encoding_CVPR_2021_paper.pdf), CVPR 2021.
- [Retentive R-CNN: Generalized Few-Shot Object Detection without Forgetting](https://openaccess.thecvf.com/content/CVPR2021/papers/Fan_Generalized_Few-Shot_Object_Detection_Without_Forgetting_CVPR_2021_paper.pdf), CVPR 2021.
- [Halluc: Hallucination Improves Few-Shot Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhang_Hallucination_Improves_Few-Shot_Object_Detection_CVPR_2021_paper.pdf), CVPR 2021.
- [StarNet: towards Weakly Supervised Few-Shot Object Detection](http://arxiv.org/abs/2003.06798), AAAI 2021.
- [Context-Transformer: Tackling Object Confusion for Few-Shot Detection](https://arxiv.org/pdf/2003.07304.pdf),AAAI 2020.
- [FSOD-ARPN-MRD: Few-Shot Object Detection With Attention-RPN and Multi-Relation Detector](https://arxiv.org/abs/1908.01998), CVPR 2020.
- [ONCE: Incremental Few-Shot Object Detection](https://openaccess.thecvf.com/content_CVPR_2020/papers/Perez-Rua_Incremental_Few-Shot_Object_Detection_CVPR_2020_paper.pdf), CVPR 2020.
- [TFA: Frustratingly Simple Few-Shot Object Detection](https://arxiv.org/abs/2003.06957), ICML 2020.
[FSDetView: Few-Shot Object Detection and Viewpoint Estimation for Objects in the Wild](https://arxiv.org/abs/2007.12107), ECCV 2020.
- [MPSR: Multi-Scale Positive Sample Refinement for Few-Shot Object Detection](https://arxiv.org/pdf/2007.09384.pdf), ECCV 2020.
- [NP-RepMet: Restoring Negative Information in Few-Shot Object Detection](https://arxiv.org/pdf/2010.11714.pdf), NeurIPS 2020.
- [Meta-RCNN: Meta Learning for Few-Shot Object Detection](https://dl.acm.org/doi/10.1145/3394171.3413832), ACM-MM 2020.