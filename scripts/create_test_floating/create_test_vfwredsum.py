import logging
import os
from scripts.test_common_info import *
import re

instr = 'vfwredsum'
rs1_val = ["0x00000000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0xBF800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0x3F800000", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0xFF7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x7F7FFFFF", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x80855555", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x00800001", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x80800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000", "0x00800000",
           "0x00800000", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x807FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x007FFFFF", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x807FFFFE", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x00000002", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x80000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x00000001", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x80000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", ]
rs2_val = ["0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000",
           "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", "0x00000000", "0xBF800000", "0x3F800000", "0xFF7FFFFF", "0x7F7FFFFF", "0x80855555", "0x00800001", "0x80800000", "0x00800000", "0x807FFFFF", "0x007FFFFF", "0x807FFFFE", "0x00000002", "0x80000001", "0x00000001", "0x80000000", ]


def generate_macros(f):
    for n in range(2,32):
        print("#define TEST_W_FP_WV_OP_DS_1%d( testnum, inst, finst, flags, val1, val2 )"%n + " \\\n\
        TEST_CASE_WVWF_FP( testnum, v14, flags, val1, val2, \\\n\
            fld f0, 0(a0); \\\n\
            flw f1, 8(a0); \\\n\
            flw f4, 8(a0); \\\n\
            VSET_DOUBLE_VSEW \\\n\
            vfmv.s.f v1, f0; \\\n\
            VSET_VSEW \\\n\
            vfmv.s.f v%d, f1;"%n+" \\\n\
            fcvt.d.s f4, f4; \\\n\
            finst f2, f0, f4; \\\n\
            inst v14, v1, v%d;"%n+" \\\n\
        )",file=f)

    for n in range(4,32,2):
        print("#define TEST_W_FP_WV_OP_DS_rd%d( testnum, inst, finst, flags, val1, val2 )"%n + " \\\n\
        TEST_CASE_WVWF_FP( testnum, v%d, flags, val1, val2,"%n+" \\\n\
            fld f0, 0(a0); \\\n\
            flw f1, 8(a0); \\\n\
            flw f4, 8(a0); \\\n\
            VSET_DOUBLE_VSEW \\\n\
            vfmv.s.f v1, f0; \\\n\
            VSET_VSEW \\\n\
            vfmv.s.f v2, f1; \\\n\
            fcvt.d.s f4, f4; \\\n\
            finst f2, f0, f4; \\\n\
            inst v%d, v1, v2;"%n+" \\\n\
        )",file=f)

    print("#define TEST_W_FP_WV_OP_DS_rd2( testnum, inst, finst, flags, val1, val2 ) \\\n\
        TEST_CASE_WVWF_FP( testnum, v2, flags, val1, val2, \\\n\
            fld f0, 0(a0); \\\n\
            flw f1, 8(a0); \\\n\
            flw f4, 8(a0); \\\n\
            VSET_DOUBLE_VSEW \\\n\
            vfmv.s.f v3, f0; \\\n\
            VSET_VSEW \\\n\
            vfmv.s.f v4, f1; \\\n\
            fcvt.d.s f4, f4; \\\n\
            finst f2, f0, f4; \\\n\
            inst v2, v3, v4; \\\n\
        )",file=f)


def extract_operands(f, rpt_path):
    # Floating pooints tests don't need to extract operands, rs1 and rs2 are fixed
    return 0


def generate_tests(f):
    n = 1
    print("  #-------------------------------------------------------------",file=f)
    print("  # vfwredosum Tests",file=f)
    print("  #-------------------------------------------------------------",file=f)
    print("  RVTEST_SIGBASE( x12,signature_x12_1)",file=f)
    for i in range(len(rs1_val)):
        n += 1
        print("  TEST_W_FP_WV_OP_DS( "+str(n)+",  vfwredosum.vs, fadd.d, 0xff100, "+rs2_val[i]+", "+rs1_val[i]+" );",file=f)

    # print("  #-------------------------------------------------------------",file=f)
    # print("  # vfwredusum Tests",file=f)
    # print("  # Raise opcode `vfwredusum.vs v14,v2,v1'",file=f)
    # print("  #-------------------------------------------------------------",file=f)
    # print("  RVTEST_SIGBASE( x20,signature_x20_0)",file=f)
    # for i in range(len(rs1_val)):
    #     n += 1
    #     print("  #TEST_W_FP_WV_OP_DS( "+str(n)+",  vfwredusum.vs, fadd.d, 0xff100, "+rs2_val[i]+", "+rs1_val[i]+" );",file=f)

    print("  #-------------------------------------------------------------",file=f)
    print("  # vfwredosum Tests (different register)",file=f)
    print("  #-------------------------------------------------------------",file=f)
    print("  RVTEST_SIGBASE( x12,signature_x12_1)",file=f)
    for i in range(len(rs1_val)):     
        k = i % 15 + 1
        n += 1
        print("  TEST_W_FP_WV_OP_DS_rd%d( "%(k*2)+str(n)+",  vfwredosum.vs, fadd.d, 0xff100, "+rs2_val[i]+", "+rs1_val[i]+" );",file=f)
        
        k = i % 30 + 2
        if (k == 14):
            continue;
        n += 1
        print("  TEST_W_FP_WV_OP_DS_1%d( "%k+str(n)+",  vfwredosum.vs, fadd.d, 0xff100, "+rs2_val[i]+", "+rs1_val[i]+" );",file=f)


def print_ending(f):
    print("  RVTEST_SIGBASE( x20,signature_x20_2)\n\
    \n\
    TEST_PASSFAIL\n\
    #endif\n\
    \n\
    RVTEST_CODE_END\n\
    RVMODEL_HALT\n\
    \n\
    .data\n\
    RVTEST_DATA_BEGIN\n\
    \n\
    TEST_DATA\n\
    \n\
    ", file=f)

    print("signature_x12_0:\n\
        .fill 0,4,0xdeadbeef\n\
    \n\
    \n\
    signature_x12_1:\n\
        .fill 32,4,0xdeadbeef\n\
    \n\
    \n\
    signature_x20_0:\n\
        .fill 512,4,0xdeadbeef\n\
    \n\
    \n\
    signature_x20_1:\n\
        .fill 512,4,0xdeadbeef\n\
    \n\
    \n\
    signature_x20_2:\n\
        .fill 376,4,0xdeadbeef\n\
    \n\
    #ifdef rvtest_mtrap_routine\n\
    \n\
    mtrap_sigptr:\n\
        .fill 128,4,0xdeadbeef\n\
    \n\
    #endif\n\
    \n\
    #ifdef rvtest_gpr_save\n\
    \n\
    gpr_save:\n\
        .fill 32*(XLEN/32),4,0xdeadbeef\n\
    \n\
    #endif\n\
    \n\
    RVTEST_DATA_END\n\
    ", file=f)


def create_empty_test_vfwredsum_b1(xlen, vlen, vsew, lmul, vta, vma, output_dir):
    logging.info("Creating empty test for {}".format(instr))

    path = "%s/%s_b1_empty.S" % (output_dir, instr)
    f = open(path, "w+")

    # Common header files
    print_common_header(instr, f)

    print("  TEST_W_FP_WV_OP_DS( 1,  vfwredosum.vs, fadd.d, 0, 1, 1);", file=f)

    # Common const information
    print_ending(f)

    f.close()
    os.system("cp %s %s" % (path, output_dir))

    logging.info(
        "Creating empty test for {}: finish in {}!".format(instr, path))

    return path


def create_first_test_vfwredsum_b1(xlen, vlen, vsew, lmul, vta, vma, output_dir, rpt_path):
    logging.info("Creating first test for {}".format(instr))

    path = "%s/%s_b1_first.S" % (output_dir, instr)
    f = open(path, "w+")

    # Common header files
    print_common_header(instr, f)

    # Extract operands
    extract_operands(f, rpt_path)

    # Generate macros to test diffrent register
    generate_macros(f)

    # Generate tests
    generate_tests(f)

    # Common const information
    print_ending(f)

    f.close()
    os.system("cp %s %s" % (path, output_dir))

    logging.info(
        "Creating first test for {}: finish in {}!".format(instr, path))

    return path